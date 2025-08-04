import socket
import re

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

# learning how to use subprocess & excute a ping


def ping (ip):
    # print(f"this what the var ip is \n{ip} ") == Was there so I could vaildate IP input from addr
    pinging = subprocess.run(["ping", "-c", "3", (ip)], capture_output=True, text=True)
    print("Did it talk to you ?:", pinging.stdout)
    print(pinging.returncode)   
    




###################################################################

network = subprocess.run(["ip","a"], capture_output=True, text=True)


##########################################################################
# This aera i need to take the output of the subprocces network to find my local IP range to give me a rang i can look into
res = []

IpLookUp = r"(192\.168\.[0-9]+\.[0-9]+)"
res = re.findall(IpLookUp, network.stdout)
print(res)

#print("DEBUG res =", res, type(res))


#print(res[0],"Trying to print res as a str",type(res[0]))

#print("This is just res but making it ip and calling the data to split",res, (type(res)))

def live_Ping (ip, c):
    ping = subprocess.run(["ping","-c",(c),(ip)],capture_output=True, text=True)
    if ping.returncode == 0:
            print(ip,"Is Alive",ping.returncode)
    else:
        print(ip, "Was not responding")

print(live_Ping("168.165.12.0","3"))         
