import socket

gethostname = socket.gethostname
gethostbyname = socket.gethostbyname
gethostbyaddress = socket.gethostbyaddr


print(f"IP address of localhost: {gethostname()}")

hostname = gethostname()
print(f" this is calling the hostname var and it is {hostname}")

print(f"IP address of {gethostbyname(hostname)}")
addr = gethostbyname(hostname)
print(f"this is calling the addr Var and it is {addr}")

print(f"IP address using gethostbyaddr {gethostbyaddress(addr)}")
