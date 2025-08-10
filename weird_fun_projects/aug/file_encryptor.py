from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from pathlib import Path
from cryptography.fernet import Fernet
import secrets



def file_c():
    file_path = askopenfilename(title="Choose your file")
    print(file_path)


key = Fernet.generate_key()  # secure random 16 bytes
toke = Fernet(key)

token = toke.encrypt(b"this is a secret message")
print(token, key)
print(toke.decrypt(token))


file_c()