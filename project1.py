import hashlib

d = input("Enter textual data: ")

print("md5 of", d, ":", hashlib.md5(d.encode()))
