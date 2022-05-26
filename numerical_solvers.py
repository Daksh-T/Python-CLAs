import time
import os

# Define the function to clear screen
def clear():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

clear()

# Loop the main screen UI
while 1==1:
    clear()
    print("Hello there!")
    print("What do you want to use today?")
    print("1. Mirror calculator")
    print("2. Lens calculator")
    print("3. Exit")
    choice = int(input("(1/2/3) "))

# Mirror calculator
    if choice == 1:
        clear()
        while 1==1:
            print("Welcome to the mirror calculator")
            print("Please enter the values with the appropriate sign!")
            f = input("What is the focal length (f) ? ")
            u = input("What is the object distance (u)? ")
            v = input("What is the mirror distance (v)? ")
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

            inp = input("Press enter to restart or q to quit ")
            if inp == "q":             
                break
            else:
                clear()

# Lens calculator
    elif choice == 2:
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

# Exit                
    elif choice == 3:
        print("Goodbye!")
        time.sleep(1)
        exit()
        
# Any input other than 1/2/3 is invalid
    else:
        input("Invalid input!")
        clear()