import os

# Ask the user for the numbers
number_1 = float(input("What's the first number? "))
number_2 = float(input("What's the second number? "))

# Define functions for the add, subtract and multiply operations
def add_numbers(n1, n2):
    sum = n1+n2
    return sum
def subtract_numbers(n1,n2):
    diff = n1-n2
    return diff
def multiply_numbers(n1,n2):
    product = n1*n2
    return product
def clear():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
    
# Main UI
#Loop the UI
while True:
    print("What do you want to do with the numbers?")
    print("1. Add them")
    print("2. Subtract them")
    print("3. Multiply them")
    print("4. Divide them")
    print("5. Change numbers")
    print("6. Exit")
    operationtouse = input("Which operation do you want to perform? (1/2/3/4/5/6) ")
    if operationtouse == "1":
        input(str(add_numbers(number_1, number_2)) + " ")
        clear()
    elif operationtouse == "2":
        input(str(subtract_numbers(number_1, number_2)) + " ")
        clear()
    elif operationtouse == "3":
        input(str(multiply_numbers(number_1, number_2)) + " ")
        clear()
    elif operationtouse == "4":
        q, r = divmod(number_1, number_2)
        if r == 0:
            input("Quotient: " + str(q) + " ")
            clear()
        else:
            print("Quotient: " + str(q))
            input("Remainder: " + str(r) + " ")
            clear()
    elif operationtouse == "5":
        number_1 = float(input("What's the first number? "))
        number_2 = float(input("What's the second number? "))
        clear()
    elif operationtouse == "6":
        break
        exit
    else:
        print("Invalid Input")