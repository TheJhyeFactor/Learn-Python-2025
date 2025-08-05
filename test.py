# 1. Convert string IP octets to integers



octet1 = "192"
octet2 = "168"

ip_1 = int(octet1) 
ip_2 = int(octet2)

print(f"converted Ip str into int: {type(ip_1)},{ip_1}, {type(ip_2)}, {ip_2}")




# Convert and verify they're valid (0-255)

if ip_2 > 0-255:
    print(f"{ip_2} is Vaild") 
    
if ip_1 > 0-255:
    print(f"{ip_1} is Vaild") 


# 2. Build an IP address from integer parts
ip_parts = [192, 168, 1, 1]

length = len(ip_parts)

#print(length)

if ip_parts >0:
    up = 0
    for num in ip_parts:
        up = up + 1
        print(length[up])
    
    #print(up)
    
   
        


ip_addr = ip_parts[+ 1]

# Convert to string format: "192.168.1.1"

# 3. Parse a port range string
port_range = "80-443"
# Extract start and end ports as integers