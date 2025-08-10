from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from pathlib import Path
from cryptography.fernet import Fernet


def file_c():
    file_path_raw = askopenfilename(title="Choose your file")
    print(f"This is the files path{file_path_raw}")
    file_path = Path(file_path_raw)
    
    file_path.exists()
    file_path.with_suffix(".txt")
    data = file_path.read_bytes()
    output_path = file_path.with_suffix(".bak")
    output_path.write_bytes(data)
    print(output_path)
    




key = Fernet.generate_key()  # secure random 16 bytes
toke = Fernet(key)

token = toke.encrypt(b"this is a secret message")
print(token, key)
print(toke.decrypt(token))


file_c()