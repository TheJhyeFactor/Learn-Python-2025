import tkinter
import cryptography
import secrets
random_bytes = secrets.token_bytes(16)  # secure random 16 bytes

print(random_bytes, type(random_bytes))