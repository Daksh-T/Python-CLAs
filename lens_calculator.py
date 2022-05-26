import time
import os

def clear():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
    
clear()

while 1==1:
    print("Welcome to the lens calculator")
    print("Please enter the values with the appropriate sign!")
    f = input("What is the focal length (f) ? ")
    u = input("What is the object distance (u)? ")
    v = input("What is the mirror distance (v)? ")
    clear()


    if v == "":
        u = float(u)
        f = float(f)
        v = (f*u)/(u+f)
        print("The value of v is ", v)
    elif u == "":
        v = float(v)
        f = float(f)
        u = (f*v)/(f-v)
        print("The value of u is ", u)
    elif f == "":
        u = float(u)
        v = float(v)
        f = (u*v)/(u-v)
        print("The value of f is ", f)
    else:
        print("Invalid input!")

    inp = input("Press enter to restart or q to quit ")
    if inp == "q":
        break
    else:
        clear()