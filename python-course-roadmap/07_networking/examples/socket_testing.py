import socket
import re

gethostname = socket.gethostname
gethostbyname = socket.gethostbyname
gethostbyaddrefined_net_resultss = socket.gethostbyaddr

print(f"IP addrefined_net_resultss of localhost: {gethostname()}")

hostname = gethostname()
print(f" this is calling the hostname var and it is {hostname}")

print(f"IP addrefined_net_resultss of {gethostbyname(hostname)}")
addr = gethostbyname(hostname)
print(f"this is calling the addr Var and it is {addr}")

print(f"IP addrefined_net_resultss using gethostbyaddr {gethostbyaddrefined_net_resultss(addr)}")

import socket
import subprocess

gethostname = socket.gethostname
gethostbyname = socket.gethostbyname
gethostbyaddrefined_net_resultss = socket.gethostbyaddr

print(f"IP addrefined_net_resultss of localhost: {gethostname()}")

hostname = gethostname()
print(f" this is calling the hostname var and it is {hostname}")

print(f"IP addrefined_net_resultss of {gethostbyname(hostname)}")

addr = gethostbyname(hostname)
print(f"this is calling the addr Var and it is {addr}")

print(f"IP addrefined_net_resultss using gethostbyaddr {gethostbyaddrefined_net_resultss(addr)}")

#############################################################

# learning how to use subprocess & excute a ping


def ping (ip):
    # print(f"this what the var ip is \n{ip} ") == Was there so I could vaildate IP input from addr
    pinging = subprocess.run(["ping", "-c", "3", (ip)], capture_output=True, text=True)
    print("Did it talk to you ?:", pinging.stdout)
    print(pinging.returncode)   
    




##################################################################

# This aera i need to take the output of the subprocces network to find my local IP range to give me a rang i can look into
refined_net_results = []
network = subprocess.run(["ip","a"], capture_output=True, text=True)

def dirty_ip (d_ip):
    for d_ip in dirty_ip: 
        dirty_ip = "(192\.168\.[0-9]+\.255)"
    return
        
IpLookUp = r"(192\.168\.[0-9]+\.[0-9]+)"
refined_net_results = re.findall(IpLookUp, network.stdout)
print("LOOK HERE BROOOO SKI THIS IS WHAT WE ARE GIVING THE IP_LIST\n",type(refined_net_results),refined_net_results)

#print("DEBUG refined_net_results =", refined_net_results, type(refined_net_results))
#print("This is just refined_net_results but making it ip and calling the data to split",refined_net_results, (type(refined_net_results)))

def live_ping (ip, c):
    ping = subprocess.run(["ping","-c",(c),(ip)],capture_output=True, text=True)
    if ping.returncode == 0:
            print(ip,"Is Alive",ping.returncode)
            return
    else:
        print(ip, "Was not refined_net_resultsponding")


def scan_ports(ip):
    return


def input_ip (ip_list):
    print(ip_list)
    
    #print("These are the IP'S split from a list",ip)
    print(len(ip_list))
    typeof_ips = type(ip_list)
    
    for ip in ip_list:
        live_ping(ip,"3")
        print(ip,"this is what we feb the ping function")
    if len(ip_list) <=0: 
        print("you dont have any ip's to talk to")
    elif typeof_ips != list:
        print("Sorry bud you are cooked !")
    


print(input_ip(refined_net_results))

#print(live_Ping("addr","3"))         






