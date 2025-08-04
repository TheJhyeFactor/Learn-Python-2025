# 🌟 Module 02A: Real-World Function Examples

## 🛡️ Security Tool Functions in Action

### Example 1: Port Scanner Function
```python
def scan_tcp_port(host, port, timeout=1):
    """
    Scan a single TCP port on a host.
    
    Args:
        host (str): Target IP or hostname
        port (int): Port number to scan
        timeout (int): Connection timeout in seconds
        
    Returns:
        tuple: (is_open, response_time, banner)
    """
    import socket
    import time
    
    start_time = time.time()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    
    try:
        result = sock.connect_ex((host, port))
        response_time = (time.time() - start_time) * 1000  # Convert to ms
        
        if result == 0:
            # Try to grab banner
            try:
                sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
                banner = sock.recv(1024).decode('utf-8', errors='ignore')
                banner = banner.split('\n')[0].strip()
            except:
                banner = ""
            
            sock.close()
            return True, response_time, banner
        else:
            sock.close()
            return False, response_time, ""
    except:
        return False, 0, ""

# Usage
is_open, time_ms, banner = scan_tcp_port("scanme.nmap.org", 80)
if is_open:
    print(f"[+] Port 80 OPEN ({time_ms:.2f}ms)")
    if banner:
        print(f"    Banner: {banner}")
```

### Example 2: IP Validation Functions
```python
def validate_ipv4(ip_string):
    """
    Validate IPv4 address format.
    
    Args:
        ip_string (str): IP address to validate
        
    Returns:
        bool: True if valid IPv4
    """
    octets = ip_string.split('.')
    
    if len(octets) != 4:
        return False
        
    for octet in octets:
        try:
            num = int(octet)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
            
    return True

def ip_to_int(ip_string):
    """Convert IP address to integer for range calculations."""
    if not validate_ipv4(ip_string):
        raise ValueError("Invalid IP address")
        
    octets = [int(x) for x in ip_string.split('.')]
    return (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8) + octets[3]

def int_to_ip(ip_int):
    """Convert integer back to IP address."""
    return f"{(ip_int >> 24) & 0xFF}.{(ip_int >> 16) & 0xFF}.{(ip_int >> 8) & 0xFF}.{ip_int & 0xFF}"

# Usage
if validate_ipv4("192.168.1.1"):
    ip_num = ip_to_int("192.168.1.1")
    print(f"IP as integer: {ip_num}")
    print(f"Back to IP: {int_to_ip(ip_num)}")
```

### Example 3: Service Detection Functions
```python
def identify_service(port, banner=""):
    """
    Identify service based on port and optional banner.
    
    Args:
        port (int): Port number
        banner (str): Optional service banner
        
    Returns:
        dict: Service information
    """
    # Common port mappings
    known_ports = {
        21: {"name": "FTP", "risk": "MEDIUM"},
        22: {"name": "SSH", "risk": "LOW"},
        23: {"name": "Telnet", "risk": "HIGH"},
        25: {"name": "SMTP", "risk": "MEDIUM"},
        80: {"name": "HTTP", "risk": "LOW"},
        443: {"name": "HTTPS", "risk": "LOW"},
        3306: {"name": "MySQL", "risk": "MEDIUM"},
        3389: {"name": "RDP", "risk": "MEDIUM"},
        5432: {"name": "PostgreSQL", "risk": "MEDIUM"}
    }
    
    service_info = known_ports.get(port, {"name": "Unknown", "risk": "UNKNOWN"})
    
    # Enhanced detection from banner
    if banner:
        banner_lower = banner.lower()
        if "apache" in banner_lower:
            service_info["server"] = "Apache"
        elif "nginx" in banner_lower:
            service_info["server"] = "Nginx"
        elif "openssh" in banner_lower:
            service_info["version"] = banner.split()[0]
    
    return service_info

def format_service_report(ip, port, service_info):
    """Format service information for reporting."""
    risk_colors = {
        "HIGH": "🔴",
        "MEDIUM": "🟡", 
        "LOW": "🟢",
        "UNKNOWN": "⚪"
    }
    
    risk_icon = risk_colors.get(service_info["risk"], "⚪")
    
    report = f"{risk_icon} {ip}:{port} - {service_info['name']}"
    
    if "server" in service_info:
        report += f" ({service_info['server']})"
    if "version" in service_info:
        report += f" [{service_info['version']}]"
        
    return report

# Usage
service = identify_service(22, "SSH-2.0-OpenSSH_8.2p1")
print(format_service_report("192.168.1.1", 22, service))
```

### Example 4: Logging Functions
```python
import datetime

def log_scan_event(event_type, target, details="", severity="INFO"):
    """
    Log security scan events with consistent formatting.
    
    Args:
        event_type (str): Type of event (SCAN_START, PORT_OPEN, etc.)
        target (str): Target IP or hostname
        details (str): Additional details
        severity (str): Log level (INFO, WARNING, ERROR)
        
    Returns:
        str: Formatted log entry
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    severity_icons = {
        "INFO": "[i]",
        "WARNING": "[!]",
        "ERROR": "[X]",
        "SUCCESS": "[✓]"
    }
    
    icon = severity_icons.get(severity, "[?]")
    
    log_entry = f"{timestamp} {icon} {event_type}: {target}"
    if details:
        log_entry += f" - {details}"
        
    return log_entry

def log_scan_summary(total_hosts, open_ports, scan_duration):
    """Generate a scan summary log entry."""
    success_rate = (len(open_ports) / total_hosts * 100) if total_hosts > 0 else 0
    
    summary = f"""
Scan Summary:
- Total Hosts: {total_hosts}
- Open Ports Found: {len(open_ports)}
- Success Rate: {success_rate:.1f}%
- Duration: {scan_duration:.2f} seconds
- Ports: {', '.join(map(str, sorted(open_ports)))}
"""
    return summary

# Usage
print(log_scan_event("SCAN_START", "192.168.1.0/24"))
print(log_scan_event("PORT_OPEN", "192.168.1.1", "Port 80 - HTTP", "SUCCESS"))
print(log_scan_event("SCAN_ERROR", "192.168.1.50", "Connection timeout", "ERROR"))
```

### Example 5: Utility Functions
```python
def sanitize_input(user_input, input_type="ip"):
    """
    Sanitize user input to prevent injection attacks.
    
    Args:
        user_input (str): Raw user input
        input_type (str): Type of input (ip, port, hostname)
        
    Returns:
        str: Sanitized input or None if invalid
    """
    import re
    
    # Remove whitespace
    cleaned = user_input.strip()
    
    if input_type == "ip":
        # Only allow valid IP characters
        if re.match(r'^[0-9.]+$', cleaned):
            return cleaned if validate_ipv4(cleaned) else None
            
    elif input_type == "port":
        # Only allow numbers
        if cleaned.isdigit():
            port = int(cleaned)
            return str(port) if 1 <= port <= 65535 else None
            
    elif input_type == "hostname":
        # Allow alphanumeric, dots, and hyphens
        if re.match(r'^[a-zA-Z0-9.-]+$', cleaned):
            return cleaned
            
    return None

def calculate_scan_eta(ports_remaining, ports_per_second):
    """Calculate estimated time of arrival for scan completion."""
    if ports_per_second <= 0:
        return "Unknown"
        
    seconds_remaining = ports_remaining / ports_per_second
    
    if seconds_remaining < 60:
        return f"{seconds_remaining:.0f} seconds"
    elif seconds_remaining < 3600:
        return f"{seconds_remaining / 60:.1f} minutes"
    else:
        return f"{seconds_remaining / 3600:.1f} hours"

# Usage
safe_ip = sanitize_input(" 192.168.1.1 ", "ip")
print(f"Sanitized IP: {safe_ip}")

eta = calculate_scan_eta(50000, 100)
print(f"Scan ETA: {eta}")
```

## 🔧 How These Functions Build Real Tools

1. **Modularity**: Each function has one clear purpose
2. **Reusability**: Functions can be used across different tools
3. **Error Handling**: Functions validate input and handle errors
4. **Documentation**: Clear docstrings explain usage
5. **Return Values**: Functions return useful data for further processing

## 💡 Best Practices Demonstrated

- Always validate input parameters
- Use descriptive function and parameter names
- Include docstrings for documentation
- Return meaningful values (not just print)
- Handle errors gracefully
- Keep functions focused on one task

---

*Study these examples to understand how functions power professional security tools!*