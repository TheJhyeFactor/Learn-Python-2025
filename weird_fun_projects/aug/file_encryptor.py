import tkinter
from cryptography.fernet import Fernet
import secrets
key = Fernet.generate_key()  # secure random 16 bytes
toke = Fernet(key)

token = toke.encrypt(b"this is a secret message")

token

print(token, key)


print(toke.decrypt(token))