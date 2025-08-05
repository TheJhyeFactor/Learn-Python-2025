# Try this and see what happens:

tool_name = "LanSpy"
version = "1.0"
# Create a banner that looks like:
# ===== LanSpy v1.0 =====
banner = f"===== {tool_name} v{version} ====="


# 2. Create a separator line of 50 dashes
separator = "-"* 50

# 3. Format an IP scan result
ip = "192.168.1.100"
status = "ONLINE"
# Create output: "[+] 192.168.1.100 - ONLINE"

output = f"[+] {ip} - {status}"


print(banner,output)