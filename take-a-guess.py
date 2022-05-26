import time
import random

print("Hello world!")
time.sleep(3)
print("Hello again!")
time.sleep(1)
print("I am thinking of a number between 1 and 10.")
time.sleep(1)
print("Take a guess.")
guess = int(input())
if guess == random.randint(1, 10):
    print("You guessed it!")
else: print("Sorry, you guessed it wrong.")