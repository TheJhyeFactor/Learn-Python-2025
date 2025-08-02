import socket
import subprocess

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

#############################################################

def ping (ip):
    print(f"this what the var ip is \n{ip} ")
    print(f"debugging {type(ip)}, type({ip})")
    pinging = subprocess.run(["ping", "-c", "3", (ip)], capture_output=True, text=True)
    print("Did it talk to you ?:", pinging.stdout)
    
print(ping(addr))
