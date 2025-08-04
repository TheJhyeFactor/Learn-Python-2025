# 🌟 Module 01: Real-World Examples

## 🛡️ Security Tool Examples Using Core Syntax

### Example 1: Banner Grabber Output
```python
# Real output from a banner grabbing tool
service_name = "OpenSSH"
version = "8.2p1"
os_info = "Ubuntu-4ubuntu0.5"

# Professional formatted output
print("="*50)
print(f"[+] Service Detected: {service_name}")
print(f"[+] Version: {version}")
print(f"[+] OS Info: {os_info}")
print("="*50)
```

### Example 2: Scan Progress Indicator
```python
# Simulating a port scan progress
current_port = 445
total_ports = 1000
percentage = (current_port / total_ports) * 100

print(f"\rScanning: Port {current_port}/{total_ports} [{percentage:.1f}%]", end="")
```

### Example 3: Vulnerability Report Header
```python
# Professional security report formatting
target_ip = "192.168.1.100"
scan_date = "2024-01-15"
risk_level = "HIGH"

report_header = f"""
╔══════════════════════════════════════════╗
║        VULNERABILITY SCAN REPORT         ║
╠══════════════════════════════════════════╣
║ Target IP:   {target_ip:<27} ║
║ Scan Date:   {scan_date:<27} ║
║ Risk Level:  {risk_level:<27} ║
╚══════════════════════════════════════════╝
"""
print(report_header)
```

### Example 4: Color-Coded Status Messages
```python
# Using ANSI escape codes for colored output
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Status messages
print(f"{GREEN}[✓]{RESET} Port 80: Open")
print(f"{RED}[✗]{RESET} Port 443: Closed")
print(f"{YELLOW}[!]{RESET} Port 8080: Filtered")
```

### Example 5: Log Entry Formatting
```python
# Security log entry format
timestamp = "2024-01-15 14:32:15"
event_type = "AUTH_FAILURE"
source_ip = "10.0.0.5"
username = "admin"

log_entry = f"[{timestamp}] {event_type}: Failed login attempt from {source_ip} for user '{username}'"
print(log_entry)
```

## 🔧 How These Examples Apply to Security Tools

1. **Banner Grabbing**: Identifying services running on open ports
2. **Progress Indicators**: Showing scan progress for long-running operations
3. **Report Headers**: Creating professional pentest reports
4. **Status Messages**: Clear visual feedback for scan results
5. **Log Formatting**: Structured logging for security events

## 💡 Pro Tips

- Use consistent formatting across your tool
- Add timestamps to all security events
- Use color coding sparingly but effectively
- Keep output clean and professional
- Always include context in your messages

---

*Study these examples to see how basic syntax creates professional security tools!*