# 🏋️ Module 02A: Functions - Exercises

## 📚 Concept 1: Basic Function Definition

### 🔍 What You'll Learn:
Functions are reusable blocks of code that perform specific tasks. They help organize code and avoid repetition.

### 📖 Example:
```python
# Simple function with no parameters
def print_banner():
    print("=" * 40)
    print("Security Scan Starting")
    print("=" * 40)

# Function with parameters
def greet_user(username):
    print(f"Welcome back, {username}")

# Function with return value
def calculate_scan_time(num_ports):
    seconds_per_port = 0.5
    total_time = num_ports * seconds_per_port
    return total_time

# Using the functions
print_banner()
greet_user("admin")
time_needed = calculate_scan_time(1000)
print(f"Estimated scan time: {time_needed} seconds")
```

### ✏️ Exercise 1.1: Create Basic Functions
```python
# 1. Create a function that prints a warning message
def print_warning():
    # TODO: Print a security warning
    pass

# 2. Create a function that takes a hostname and prints it
def display_target(hostname):
    # TODO: Print "Scanning target: [hostname]"
    pass

# 3. Create a function that returns the current scan status
def get_scan_status():
    # TODO: Return "ACTIVE" or "IDLE"
    pass

# Test your functions
print_warning()
display_target("192.168.1.1")
status = get_scan_status()
print(f"Current status: {status}")
```

---

## 📚 Concept 2: Functions with Multiple Parameters

### 🔍 What You'll Learn:
Functions can accept multiple parameters and perform complex operations.

### 📖 Example:
```python
# Multiple parameters
def scan_port(ip_address, port_number, timeout=1):
    print(f"Scanning {ip_address}:{port_number} (timeout: {timeout}s)")
    # In real code, actual scanning would happen here
    return "OPEN"  # or "CLOSED"

# Default parameter values
def create_report(scan_type="FULL", output_format="TXT"):
    print(f"Creating {scan_type} scan report in {output_format} format")

# Using the functions
result = scan_port("192.168.1.1", 80)
print(f"Port 80 is {result}")

scan_port("192.168.1.1", 443, timeout=2)
create_report()
create_report("QUICK", "PDF")
```

### ✏️ Exercise 2.1: Multi-Parameter Functions
```python
# 1. Create a function to validate IP and port
def validate_target(ip, port):
    # TODO: Check if IP has 4 octets and port is 1-65535
    # Return True if valid, False otherwise
    pass

# 2. Create a function with default timeout
def ping_host(hostname, count=4, timeout=1):
    # TODO: Print "Pinging [hostname] [count] times with [timeout]s timeout"
    pass

# 3. Create a function that formats scan results
def format_result(ip, port, status, response_time=None):
    # TODO: Return formatted string like:
    # "192.168.1.1:80 - OPEN (12ms)" or "192.168.1.1:80 - CLOSED"
    pass

# Test your functions
```

---

## 📚 Concept 3: Return Values and Multiple Returns

### 🔍 What You'll Learn:
Functions can return values for use in other parts of your program. They can even return multiple values.

### 📖 Example:
```python
# Returning a single value
def is_private_ip(ip_address):
    """Check if IP is in private range"""
    if ip_address.startswith("192.168."):
        return True
    elif ip_address.startswith("10."):
        return True
    elif ip_address.startswith("172."):
        # Simplified check
        return True
    return False

# Returning multiple values
def analyze_port(port_number):
    """Analyze port and return info"""
    well_known = port_number < 1024
    common_services = {
        80: "HTTP",
        443: "HTTPS",
        22: "SSH",
        21: "FTP"
    }
    service = common_services.get(port_number, "Unknown")
    return well_known, service

# Using the returns
ip = "192.168.1.1"
if is_private_ip(ip):
    print(f"{ip} is a private IP")

is_privileged, service_name = analyze_port(80)
print(f"Port 80: Privileged={is_privileged}, Service={service_name}")
```

### ✏️ Exercise 3.1: Working with Return Values
```python
# 1. Create a function that checks port risk level
def get_port_risk(port):
    # TODO: Return "HIGH" for ports like 23 (telnet), 135 (RPC)
    # Return "MEDIUM" for 21 (FTP), 3389 (RDP)
    # Return "LOW" for 80, 443
    # Return "UNKNOWN" for others
    pass

# 2. Create a function that returns scan statistics
def calculate_stats(open_ports, closed_ports, filtered_ports):
    # TODO: Return total ports and success percentage
    # Return as: total, percentage_open
    pass

# 3. Create a function that parses an IP address
def parse_ip(ip_string):
    # TODO: Split IP and return octets as integers
    # "192.168.1.1" -> return 192, 168, 1, 1
    pass

# Test your functions
```

---

## 📚 Concept 4: Function Scope and Documentation

### 🔍 What You'll Learn:
Variables inside functions have local scope. Good documentation makes functions reusable.

### 📖 Example:
```python
# Global variable
scan_count = 0

def perform_scan(target):
    """
    Perform a security scan on the target.
    
    Args:
        target (str): IP address or hostname to scan
        
    Returns:
        dict: Scan results with open ports and services
    """
    # Local variable
    start_time = "10:30:00"
    
    # Accessing global variable
    global scan_count
    scan_count += 1
    
    print(f"Scan #{scan_count} started at {start_time}")
    print(f"Scanning {target}...")
    
    # Local variable not accessible outside
    results = {"ports": [80, 443], "status": "completed"}
    return results

# Using the function
result = perform_scan("192.168.1.1")
print(f"Total scans performed: {scan_count}")
# print(start_time)  # This would cause an error - start_time is local
```

### ✏️ Exercise 4.1: Scope and Documentation
```python
# Global configuration
verbose_mode = False
total_hosts_scanned = 0

# 1. Create a well-documented function
def scan_network(network_range, ports=[80, 443]):
    """
    TODO: Add proper documentation
    - Describe what the function does
    - Document parameters
    - Document return value
    """
    global total_hosts_scanned
    # TODO: Increment total_hosts_scanned
    # TODO: Use verbose_mode to control output
    pass

# 2. Create a function with local variables
def generate_report():
    # TODO: Create local variables for:
    # - report_id (random number)
    # - timestamp (current time string)
    # - Return formatted report header
    pass

# 3. Create a configuration function
def set_verbose(enabled):
    """Enable or disable verbose output"""
    # TODO: Modify global verbose_mode
    pass

# Test scope behavior
```

---

## 🎯 Practice Challenge

Create a Port Service Identifier:

```python
# Build these functions:
# 1. is_web_port(port) - returns True for 80, 443, 8080, 8443
# 2. is_database_port(port) - returns True for 3306, 5432, 1433, 27017
# 3. get_service_category(port) - returns "web", "database", "remote", or "other"
# 4. format_service_info(ip, port) - returns formatted string with all info

# Example usage:
# info = format_service_info("192.168.1.1", 3306)
# Should return: "192.168.1.1:3306 [DATABASE - MySQL]"

# Your implementation:
```

---

## 📝 Reflection Questions

1. When should you use return vs print in a function?
2. Why are default parameters useful in security tools?
3. How does function scope help prevent bugs?

---

*Complete all exercises before moving to the mini-project!*