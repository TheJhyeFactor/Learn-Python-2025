##### This project i am going to take a url from a user 
#####I am going to then scan that URL to see what ports are open
##### Then i am going to tell the user what ports are open 


class website_scan:
    url = (input(f"Welcome what website do you want to scantoday:\n PLEASE NOTE MUST ENTER FULL URL e.g: https://XYZ.com\n"))
    url_confirm = input(f"Are you sure you want to scan this website ?{url}\n Y(yes) | N(No)")
    print(url, url_confirm)

website_scan