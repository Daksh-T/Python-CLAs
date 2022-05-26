import time
import os

def clear():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
    
clear()
print("Welcome to the mirror calculator.")
print("Please enter the values with the appropriate sign!")
u = input("What is the object distance (u)? ")
v = input("What is the mirror distance (v)? ")
f = input("What is the focal length (f) ? ")
clear()


if v == "":
    u = float(u)
    f = float(f)
    v = (f*u)/(u-f)
    print("The value of v is ", v)
elif u == "":
    v = float(v)
    f = float(f)
    u = (f*v)/(v-f)
    print("The value of u is ", u)
elif f == "":
    u =float(u)
    v =float(v)
    f = (u*v)/(v+u)
    print("The value of f is ", f)
else:
    print("Invalid input!")

input("Press enter to close")