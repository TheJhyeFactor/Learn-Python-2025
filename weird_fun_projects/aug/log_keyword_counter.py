"""
📋 Objective
Write a small script that:

Accepts:Path to a text “log” fileA keyword to search for

Opens the file safely:Counts how many times that keyword appears (across all lines)

Handles errors (e.g. file not found)
Prints the final tally of total keywords
"""

from tkinter import Tk
from tkinter.filedialog import askopenfilename

def file_path(key):
    key
    path = askopenfilename(title='Select file') # shows dialog box and return the path
    print(path)
    read_file(path,key)

def keyword():
    key = input(str("Please input the Keyword you would like to find: "))
    file_path(key)
    
def read_file(path,key):
    key
    read_txt = open(f"{path}"r"")
    print(F"So this is the Read_Text,{read_txt}")
    key_wrd_c = read_txt.read()
    key_count = key_wrd_c.count(key)
    print(read_txt.read)
    results(key,key_count)
    
    
def results(key,key_count):
    print(f"Total number of times,{key}, Was found,{key_count}")
    
    
    
    
keyword()
