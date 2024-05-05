import random

def numeric(passlen):
    s="01234567890"
    password =  "".join(random.sample(s,passlen ))
    return password
    
def aphabetic(passlen):
    s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password =  "".join(random.sample(s,passlen))
    return password

def alphanumeric(passlen):
    s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password =  "".join(random.sample(s,passlen))
    return password

def specialcase(passlen):
    s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password =  "".join(random.sample(s,passlen))
    return password

def choice(passtype, passlen):
    if passtype == 1:
        return numeric(passlen)
    
    elif passtype == 2:
        return aphabetic(passlen)
        
    elif passtype == 3:
        return alphanumeric(passlen)
        
    elif passtype == 4:
        return specialcase(passlen)
     
    else:
        print("Invalid Option Selected... Try Again...")
        return password()
        
def password():
    passlen = int(input("Enter the length of password: ")) # Length of the Password
    print("Enter Password Type: \n1. Numeric \n2. Alphabetic \n3. Alpha-Numeric \n4. Special Case")
    passtype = int(input("Enter Option: "))
    return choice(passtype,passlen)


password = password()
print("Password x-----   ",password,"   ------x")

