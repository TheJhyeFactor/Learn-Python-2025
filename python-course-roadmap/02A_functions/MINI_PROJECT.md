# 🚀 Module 02A: Mini-Project - Security Utilities Library

## 📋 Project Overview

Create a comprehensive security utilities library with functions for IP validation, port analysis, and network calculations that can be reused across different security tools.

## 🎯 Project Goals

Build a `security_utils.py` module containing:
1. IP address validation and manipulation functions
2. Port security analysis functions  
3. Network range calculation functions
4. Service identification functions
5. Risk assessment functions

## 📝 Requirements

Your library must include:
- [ ] At least 8 different utility functions
- [ ] Proper documentation for each function
- [ ] Input validation and error handling
- [ ] Return meaningful values (not just print)
- [ ] Functions that work together

## 🏗️ Project Structure

```python
# security_utils.py
"""
Security Utilities Library
A collection of functions for network security operations
"""

def validate_ip(ip_address):
    """
    Validate if a string is a valid IPv4 address.
    
    Args:
        ip_address (str): IP address to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    # TODO: Implement validation
    pass

def is_private_ip(ip_address):
    """
    Check if IP is in private range (RFC 1918).
    
    Args:
        ip_address (str): IP address to check
        
    Returns:
        bool: True if private, False if public
    """
    # TODO: Check 10.x, 172.16-31.x, 192.168.x
    pass

# Add more functions...
```

## 📊 Required Functions

### 1. IP Address Functions
```python
def validate_ip(ip_address):
    """Validate IPv4 address format"""
    # Check format: x.x.x.x where x is 0-255
    pass

def is_private_ip(ip_address):
    """Check if IP is in private range"""
    # 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
    pass

def get_ip_class(ip_address):
    """Return IP class (A, B, C, D, E)"""
    # Based on first octet
    pass
```

### 2. Port Analysis Functions
```python
def validate_port(port):
    """Check if port number is valid (1-65535)"""
    pass

def get_port_risk_level(port):
    """Return risk level: HIGH, MEDIUM, LOW"""
    # HIGH: telnet(23), netbios(135-139)
    # MEDIUM: ftp(21), rdp(3389)
    # LOW: http(80), https(443)
    pass

def is_privileged_port(port):
    """Check if port requires root/admin (< 1024)"""
    pass
```

### 3. Service Identification Functions
```python
def identify_service(port):
    """Return service name for common ports"""
    # Dictionary lookup for port -> service
    pass

def get_service_category(port):
    """Return category: web, database, remote, mail, etc."""
    pass
```

### 4. Network Calculation Functions
```python
def calculate_network_range(ip_address, subnet_mask):
    """Calculate network address and broadcast"""
    # Return tuple: (network, broadcast)
    pass

def count_hosts_in_subnet(subnet_mask):
    """Calculate number of usable hosts"""
    # 2^(32-mask_bits) - 2
    pass
```

### 5. Formatting Functions
```python
def format_scan_target(ip, port_list):
    """Format target for display"""
    # "192.168.1.1 -> Ports: 80, 443, 8080"
    pass

def format_risk_assessment(ip, risks):
    """Create risk summary string"""
    pass
```

## 🎨 Bonus Challenge Functions

```python
def ip_in_range(ip, start_ip, end_ip):
    """Check if IP is within range"""
    pass

def generate_ip_range(start_ip, end_ip):
    """Generate list of IPs in range"""
    pass

def estimate_scan_time(num_hosts, num_ports, timeout=1):
    """Calculate estimated scan duration"""
    pass
```

## 📁 Complete Implementation Example

Here's one function fully implemented as a guide:

```python
def validate_ip(ip_address):
    """
    Validate if a string is a valid IPv4 address.
    
    Args:
        ip_address (str): IP address to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    Example:
        >>> validate_ip("192.168.1.1")
        True
        >>> validate_ip("256.1.1.1")
        False
    """
    if not isinstance(ip_address, str):
        return False
        
    octets = ip_address.split('.')
    
    # Must have exactly 4 octets
    if len(octets) != 4:
        return False
    
    # Each octet must be 0-255
    for octet in octets:
        try:
            num = int(octet)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
    
    return True
```

## 🧪 Testing Your Library

Create a test script:

```python
# test_security_utils.py
from security_utils import *

# Test IP validation
print("Testing IP Validation:")
test_ips = ["192.168.1.1", "256.1.1.1", "10.0.0.1", "invalid"]
for ip in test_ips:
    print(f"{ip}: Valid={validate_ip(ip)}, Private={is_private_ip(ip)}")

# Test port analysis
print("\nTesting Port Analysis:")
test_ports = [22, 80, 443, 23, 3389, 99999]
for port in test_ports:
    if validate_port(port):
        print(f"Port {port}: {identify_service(port)} - Risk: {get_port_risk_level(port)}")

# Test your other functions...
```

## ✅ Success Criteria

Your library is complete when:
1. All required functions are implemented
2. Functions have proper documentation
3. Input validation prevents errors
4. Functions return useful values
5. Test script demonstrates all functions

## 💡 Tips

- Start with simple functions and build up
- Test each function as you write it
- Think about edge cases (empty strings, None, etc.)
- Make functions work together (one's output feeds another's input)
- Keep functions focused - one task per function

## 📤 Submission

Save your completed project as:
- `02A_functions/mini_project/security_utils.py`
- `02A_functions/mini_project/test_security_utils.py`

## 🤔 Reflection Questions

After completing the project:
1. Which function was most challenging to implement?
2. How would you extend this library for a real penetration testing tool?
3. What other utility functions would be useful?

---

*This project creates a reusable security library you can use in future modules!*