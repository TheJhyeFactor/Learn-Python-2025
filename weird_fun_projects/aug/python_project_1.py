##### This project i am going to take a url from a user 
#####I am going to then scan that URL to see what ports are open
##### Then i am going to tell the user what ports are open 
import subprocess

def user_input(url):
        url = (input(f"Welcome what website do you want to scantoday:\n PLEASE NOTE MUST ENTER FULL URL e.g: https://XYZ.com\n"))
        url_confirm = input(f"Are you sure you want to scan this website ?{url}\n Y(yes) | N(No)")
        print(url_confirm)  
        if url_confirm == "yes":
            print("we are getting this far")
            website_validation(url)
        elif url_confirm == "no":
            user_input()
        
        #print(self.url, self.url_confirm) #This is a debugging methoed to few input.

def website_validation(url):
        url = user_input(url_confirm)
        ping = subprocess.run(["ping",(url)],capture_output=True,text=True)
        print(ping.stdout)


user_input