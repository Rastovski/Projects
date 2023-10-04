#!/bin/env python3
import sys, getpass, os
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA512
from Crypto.Protocol.KDF import PBKDF2

def write_data(data):
    with open("login.txt", "w") as wfile:
        for line in data:
            wfile.write(line+"\n")
    
def read_data():

    f=open("login.txt", "r")
    data=f.read().split("\n")
    data = list(filter(None, data))
    f.close()

    return data

def hash_function(passwd, user):

    salt = get_random_bytes(16).hex()
    tmp = passwd+salt
    hashed=PBKDF2(bytes(tmp.encode()), salt, 64, count=1000000, hmac_hash_module=SHA512)
    
    return salt, hashed

def add_user(paswd, user):

    salt, hashed = hash_function(paswd, user)
    
    f = open("login.txt", "a")
    f.write(f"{user} F {salt}{hashed.hex()}\n")
    f.close()

def check(passwd, provjera):

    salt = (provjera[:32])
    tmp = passwd+salt
    hashed=PBKDF2(bytes(tmp.encode()), salt, 64, count=1000000, hmac_hash_module=SHA512)
        
    if(salt+hashed.hex()==provjera):
        return True
    else:
        return False  
    
def passwd_change(paswd, user):

    salt, hashed = hash_function(paswd, user)

    data = read_data()

    for br,i in enumerate(data):
        if(i.split(" ")[0]==user):
            if(check(paswd, i.split(" ")[2])):
                print("The new password must be different from the old password!")
                sys.exit()
            data[br]=f"{user} F {salt}{hashed.hex()}"

    write_data(data)

def force_pass(user):

    data = read_data()

    for br,i in enumerate(data):
        name=i.split(" ")
        if(name[0]==user):
            name[1]="T"
            data[br]=" ".join(name)

    write_data(data)

def remove(user):

    data = read_data()

    for br,i in enumerate(data):
        name=i.split(" ")
        if(name[0]==user):
            del data[br]
    
    write_data(data)

if __name__ == "__main__":

    args = sys.argv
    action = args[1]
    user=args[2]

    
    if(action=="forcepass"):
        force_pass(user)
        print("User will be requested to change password on next login.")
    elif(action=="del"):
        remove(user)
        print("User successfuly removed.")
    else:

        password = getpass.getpass('Password: ', stream = None)

        if (len(password.rstrip())<8):
            print("Password too short. At least 8 characters!")
            sys.exit()

        repeat = getpass.getpass('Repeat password: ', stream=None)

        if(password != repeat):
            if(action=="add"):
                print("User add failed. Password mismatch.")
            elif(action=="passwd"):
                print("Password change failed. Password mismatch")
        else:
            if(action=="add"):
                add_user(password, user)
                print("User add successfuly added.")
            elif(action=="passwd"):
                passwd_change(password, user)
                print("Password change successful.")
        
    