# python code to grant access to user irrespective of letter type that is uppercase or lowercase
password="rose"
valid_password=" "
while valid_password !=password:
    valid_password=input("Enter password: ")
    valid_password=valid_password.lower()
print("Access granted")


