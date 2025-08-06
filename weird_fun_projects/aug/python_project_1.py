##### This project i am going to take a url from a user 
#####I am going to then scan that URL to see what ports are open
##### Then i am going to tell the user what ports are open 
import subprocess
import socket

live = int

port_a = [21, 22, 23, 80, 433, 3306, 5432, 8080, 8443, 9200, 6379]

ports = {
    "FTP": 21,
    "SSH": 22,
    "Telnet": 23,
    "HTTP": 80,
    "HTTPS": 443,
    "MySQL": 3306,
    "PostgreSQL": 5432,
    "http-alt / Proxies": 8080,
    "https-alt / Panels": 8443,
    "Elasticsearch": 9200,
    "Redis": 6379,
}


def user_input():
        url = (input(f"Welcome what website do you want to scantoday:\n PLEASE NOTE MUST ENTER FULL URL e.g: google.com\n"))
        url_confirm = input(f"Are you sure you want to scan this website ?{url}\n Y(yes) | N(No)")
        print(url)
        print(url_confirm)  
        if url_confirm == "yes":
            print("we are getting this far")
            website_validation(url)
        elif url_confirm == "no":
            user_input()
        
        #print(self.url, self.url_confirm) #This is a debugging methoed to few input.

def website_validation(url):
        print(f"well here we are\n{url} ")
        ping = subprocess.run(["ping","-c","3",(url)],capture_output=True,text=True)
        print(ping.stdout,ping.returncode)
        if ping.returncode == 0:
            live = 1
            print("Your website is about to be scanned")
            for p in port_a:
                port_scan(url, p)
        else:
            live = 0
            print("Your Website cant be contacted please try again")
            return user_input()


def port_scan(url, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket
        s.settimeout(1)                                       # Set timeout (1 second)
        s.connect((url, port))                                # Connect to (host, port)
        print(f"Port {port} is OPEN")
    except:
        print(f"Port {port} is CLOSED or FILTERED")
    finally:
        s.close()  




user_input()