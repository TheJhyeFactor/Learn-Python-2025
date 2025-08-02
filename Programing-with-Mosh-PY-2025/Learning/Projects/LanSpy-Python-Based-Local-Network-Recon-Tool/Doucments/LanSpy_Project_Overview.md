
# 🧪 LanSpy: A Python-Based Local Network Recon Tool

## 🎯 Project Goal

Create a Python script that:
- Detects your local IP and subnet automatically
- Builds a list of IPs on the same local network
- Performs a ping sweep to find live hosts
- Scans common TCP ports (21, 22, 80, 443) on live hosts
- Grabs service banners from open ports (if available)
- Prints a clean summary report to the terminal

---

## 🧠 Learning Objectives

- Use Python for low-level network automation
- Understand local networking: IPs, ports, services
- Apply `socket`, `subprocess`, and `ipaddress` modules
- Structure logic with functions
- Handle real-world I/O, errors, and scanning tasks

---

## 📁 File Structure (Recommended)

```
LanSpy/
├── lanspy.py              # Your main tool script
├── README.md              # This file
└── requirements.txt       # Optional: third-party modules
```

---

## 📋 Requirements

You must:
- [x] Auto-detect the subnet (no user input for target IPs)
- [x] Ping each IP in subnet
- [x] Scan 4+ ports on each live IP
- [x] Grab banners (or attempt to)
- [x] Print clean results
- [x] Use functions to organize your code
- [x] Include this README file

Optional:
- Save results to file
- Color output (e.g., `colorama`)
- Add threading for speed
- Add command-line options

---

## 🧪 Example Output

```
[+] Live Host Found: 192.168.1.45
    - Port 22 OPEN – Banner: "SSH-2.0-OpenSSH_8.2"
    - Port 80 OPEN – Banner: "Apache/2.4.41 (Ubuntu)"

[+] Live Host Found: 192.168.1.102
    - Port 443 OPEN – Banner: "nginx"

Scan Complete. 2 Hosts found. 3 total ports open.
```

---

## 🔍 Research Topics

- How to get your IP address with `socket`
- How to use `ipaddress.IPv4Network()` to generate IP ranges
- How to use `subprocess` or `os` to run ping commands
- How `socket.connect_ex()` and `recv()` work for scanning
- How to structure clean Python CLI tools

---

## 🧠 Study & Build Flow

1. **Detect local IP and subnet**
2. **Generate all usable host IPs in that subnet**
3. **Ping each IP and store which ones respond**
4. **Scan common ports (21, 22, 80, 443) on each live IP**
5. **Try to receive a banner if port is open**
6. **Print or save results**
7. **Test and clean up your code**

---

## 🧠 Reflective Questions

- How did you discover your own IP and subnet range?
- What was the hardest part of the scanning process?
- Did any ports return unexpected data?
- What would you add to this tool in version 2?

---

Good luck — and test responsibly. This tool is for use **only on networks you control**.
