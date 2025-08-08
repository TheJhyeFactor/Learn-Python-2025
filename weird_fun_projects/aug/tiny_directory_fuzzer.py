"""
Objective
Probe a base URL with a small wordlist (20 to 50 words).
For each word, request /<word> using HTTP HEAD and report non-404 responses (e.g., 200/301/302/403). 
Optional: try simple extensions like .php, .bak, .old.

"""
import subprocess
import requests
import socket

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
    y_n = input(f"Can you please confrim you ment: {base_url}: \n Please enter Y(yes) or N(no): \n Enter:")
    if y_n == "y":
        url_scan(base_url,wrd_lst)
    elif y_n == "n":
        base_url()


def url_scan(url, wrd_lst):
    r = requests.get(f"{url}{wrd_lst}")
    print(r.text)


        
user_input()