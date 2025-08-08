"""
Objective
Probe a base URL with a small wordlist (20 to 50 words).
For each word, request /<word> using HTTP HEAD and report non-404 responses (e.g., 200/301/302/403). 
Optional: try simple extensions like .php, .bak, .old.

"""
import subprocess
import requests
import time

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
        f_url = url + wrd
        #print(f_url)
        time.sleep(1.2)
        r = requests.get(f"{f_url}{wrd}")
        print(r.text)


        
user_input()