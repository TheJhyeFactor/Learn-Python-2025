"""
📋 Objective
Write a small script that:

Accepts:Path to a text “log” fileA keyword to search for

Opens the file safely:Counts how many times that keyword appears (across all lines)

Handles errors (e.g. file not found)
Prints the final tally of total keywords
"""

import os
import re

from tkinter import Tk
from tkinter.filedialog import askopenfilename
path = askopenfilename(title='Select Folder') # shows dialog box and return the path
print(path)  




def keyword():
    key = input(str("Please input the Keyword you would like to find"))
    