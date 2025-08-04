# 🏋️ Module 01: Core Syntax - Exercises

## 📚 Concept 1: Variables and Data Types

### 🔍 What You'll Learn:
Variables are containers that store data values. Python has several basic data types.

### 📖 Example:
```python
# String variable
name = "Alice"
print(f"Hello, {name}")

# Integer variable
age = 25
print(f"Age: {age}")

# Float variable
height = 5.7
print(f"Height: {height} feet")

# Boolean variable
is_student = True
print(f"Student status: {is_student}")
```

### ✏️ Exercise 1.1: Variable Practice
Create variables for:
1. Your favorite security tool name (string)
2. Number of ports to scan (integer)
3. Success rate percentage (float)
4. Is scan complete (boolean)

```python
# Your code here:
tool_name = 
ports_to_scan = 
success_rate = 
scan_complete = 

# Print them all with descriptive messages
```

---

## 📚 Concept 2: String Operations

### 🔍 What You'll Learn:
Strings can be manipulated in many ways - concatenated, repeated, sliced, and formatted.

### 📖 Example:
```python
# String concatenation
first = "Python"
second = "Security"
combined = first + " " + second
print(combined)  # Output: Python Security

# String repetition
alert = "ALERT! " * 3
print(alert)  # Output: ALERT! ALERT! ALERT! 

# String formatting
ip = "192.168.1.1"
port = 80
message = f"Scanning {ip}:{port}"
print(message)
```

### ✏️ Exercise 2.1: String Manipulation
```python
# 1. Create a banner for your security tool
tool_name = "LanSpy"
version = "1.0"
# Create a banner that looks like:
# ===== LanSpy v1.0 =====

# 2. Create a separator line of 50 dashes
separator = 

# 3. Format an IP scan result
ip = "192.168.1.100"
status = "ONLINE"
# Create output: "[+] 192.168.1.100 - ONLINE"
```

---

## 📚 Concept 3: Print Function Mastery

### 🔍 What You'll Learn:
The print function has many options for formatting output.

### 📖 Example:
```python
# Basic print
print("Simple message")

# Print with separator
print("IP", "192.168.1.1", "Port", "80", sep=" : ")

# Print without newline
print("Scanning", end="")
print("...")  # Appears on same line

# Print multiple lines
print("""
Multi-line
Security
Report
""")
```

### ✏️ Exercise 3.1: Formatted Output
```python
# 1. Print a progress indicator
# Output: Scanning port 80... [OK]
port = 80
status = "OK"

# 2. Print a table header
# Output: IP Address     | Status | Response Time

# 3. Create a loading animation (print dots on same line)
# Output: Loading...
```

---

## 📚 Concept 4: Type Conversion

### 🔍 What You'll Learn:
Converting between different data types is essential for processing user input.

### 📖 Example:
```python
# String to integer
port_string = "8080"
port_number = int(port_string)
print(f"Scanning port {port_number}")

# Integer to string
count = 5
message = "Found " + str(count) + " open ports"
print(message)

# Getting type information
print(type(port_string))  # <class 'str'>
print(type(port_number))  # <class 'int'>
```

### ✏️ Exercise 4.1: Type Conversion Practice
```python
# 1. Convert string IP octets to integers
octet1 = "192"
octet2 = "168"
# Convert and verify they're valid (0-255)

# 2. Build an IP address from integer parts
ip_parts = [192, 168, 1, 1]
# Convert to string format: "192.168.1.1"

# 3. Parse a port range string
port_range = "80-443"
# Extract start and end ports as integers
```

---

## 🎯 Practice Challenge

Combine all concepts to create a simple network scan header:

```python
# Create output that looks like this:
# =====================================
# === NetworkScanner v2.1 Starting ===
# =====================================
# Target: 192.168.1.0/24
# Ports: 80, 443, 8080
# Scan Type: TCP SYN
# =====================================

# Your code here:
```

---

## 📝 Reflection Questions

1. Which string formatting method do you prefer and why?
2. When would you use string repetition in a real tool?
3. Why is type conversion important for user input?

---

*Complete all exercises before moving to the mini-project!*