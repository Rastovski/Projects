#!/bin/env python3
import sys, getpass
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA512
from Crypto.Protocol.KDF import PBKDF2
import time

def authorize(user, passwd, check):

    salt = (check[:32])
    tmp = passwd+salt

    hashed=PBKDF2(bytes(tmp.encode()), salt, 64, count=1000000, hmac_hash_module=SHA512)  

    if(salt+hashed.hex()==check):
        return True
    else:
        return False

def change_passwd(user, provjera):

    New_Password = getpass.getpass('New password: ', stream = None)

    if (len(New_Password.rstrip())<8):
            print("Password too short. At least 8 characters!")
            sys.exit()

    New_Password_Repeat = getpass.getpass('Repeat new password: ', stream = None)

    if(New_Password!=New_Password_Repeat):
        print("Password change failed. Password mismatch")
    else:
        if(authorize(user, New_Password, provjera)):
            print("The new password must be different from the old password.")
            sys.exit()

        salt = get_random_bytes(16).hex()
        tmp = New_Password+salt
        hashed=PBKDF2(bytes(tmp.encode()), salt, 64, count=1000000, hmac_hash_module=SHA512)    

        return f"{user} F {salt}{hashed.hex()}"
    
    return "fail"
    
def login(user, passwd):

    f=open("login.txt", "r")
    data=f.read().split("\n")
    data = list(filter(None, data))
    f.close()

    for br,name in enumerate(data):
        check=name.split(" ")

        if(check[0]==user):
            if(authorize(user, passwd, check[2])):
                if(check[1]=="T"):

                    rez=change_passwd(user, check[2])

                    if(rez=="fail"):
                        return True
                    else:
                        data[br]=rez
                        with open("login.txt", "w") as wfile:
                            for line in data:
                                wfile.write(line+"\n")

                print("Login successful.")
                return True
            
            else:
                return False
    
if __name__ == "__main__":

    args = sys.argv
    user=args[1]
    i=1

    while(True):

        password = getpass.getpass('Password: ', stream = None)

        if(login(user, password)):
            break

        else:
            print("Username or password incorrect.")
            time.sleep(i)
            i = i*2