import hashlib

ha = hashlib.sha256()

message = input("Please input your meesage you would like to Hash: ")
messageB = bytes(message, "utf-16")
messageB = ha.hexdigest()

print(messageB)

print(ha)