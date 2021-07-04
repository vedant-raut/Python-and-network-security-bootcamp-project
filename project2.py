import hashlib


d = input("Enter textual data: ")

print("blake2b of", d, ":", hashlib.blake2b(d.encode()))
print("sha1 of", d, ":", hashlib.sha1(d.encode()))
print("sha224 of", d, ":", hashlib.sha224(d.encode()))
