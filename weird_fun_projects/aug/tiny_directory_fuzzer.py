"""
Objective
Probe a base URL with a small wordlist (20 to 50 words).
For each word, request /<word> using HTTP HEAD and report non-404 responses (e.g., 200/301/302/403). 
Optional: try simple extensions like .php, .bak, .old.

"""
import requests
import time
from bs4 import BeautifulSoup


reply_code = {
    200: "OK (exists)",
    204: "No Content (exists)",
    206: "Partial Content (exists)",
    301: "Moved Permanently (redirect)",
    302: "Found (redirect)",
    303: "See Other (redirect)",
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    400: "Bad Request (exists, needs params?)",
    401: "Unauthorized (auth required)",
    403: "Forbidden (exists, blocked)",
    405: "Method Not Allowed (try GET)",
    410: "Gone (used to exist)",
    429: "Too Many Requests (rate limited)",
    500: "Internal Server Error",
    501: "Not Implemented (e.g., HEAD unsupported)",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    404: "Not Found,This page does not exist"
}


r = [""]

wrd_lst = [
    "admin","login","logout","signin","signup","account","user","users","profile",
    "settings","config","setup","install","update","manage","panel","dashboard",
    "console","portal","reports","report","stats","status","health","api","v1","v2",
    "test","dev","staging","backup","backups","old","archive","tmp","uploads","upload",
    "files","images","img","assets","static","media","docs","readme","changelog",
    "license","sitemap","robots","private","internal","secure","auth","session","token",
    "keys","db","database","logs","log","error","debug","monitor","metrics","cache",
    "public","src","app","lib","www","index","contact","support","help"
]


def user_input():
    base_url = input("Please type the url you are wanting to scan: ")
    confrim = input(f"Can you please confrim you ment: {base_url}: \n Please enter Y(yes) or N(no): \n Enter:")
    y_n = confrim.lower()
    if y_n == "y":
        url_scan(base_url,wrd_lst)
    elif y_n == "n":
        base_url()


def url_scan(url,wrd_lst):
    for wrd in wrd_lst:
        
        f_url = url + wrd # Url we use to request the head
        r = requests.head(f"{f_url}")
        
        url_status = r.status_code       
        
        if r.status_code in reply_code:
            print(f"This is the Final URL {f_url}: this is out request head Status code {r.status_code}, This is the status is: {url_status}")
        else:
            print(f"This Status code {r.status_code} Wasnt in the Dicatrnery of Reply codes {reply_code}")
            print("we are still not able to cross check the status code with the reply codes key")




               
        
user_input()

""""
        time.sleep(5)
        if r.status_code in reply_code.keys():
            print(f"We are able to see the: {f_url}:\n{sat_code}")
        else:
            print(f"{f_url}:\nWe are unable to review the reply code")
            """