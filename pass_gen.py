import random
passlen = int(input("Enter password length:"))
s="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&12345678908"
password = "".join(random.sample(s,passlen))
print(password)