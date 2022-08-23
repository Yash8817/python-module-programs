email = input("Enter email :").strip()
username = email[:email.index("@")]
domain = email[email.index("@")+1 :]

print("Username:",username)               
print("Domain:",domain)
