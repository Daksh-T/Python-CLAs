import psutil
import time
import os

# Define function to clear the screen
def clear():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

# loop the UI
while True:
    print("Your current CPU Usage is: ")
    print(psutil.cpu_percent(), "%")
    print("Your current RAM Usage is: ")
    print(psutil.virtual_memory().percent, "%")
    print("Your storage usage is: ")
    print(psutil.disk_usage('/').percent, "%")
    time.sleep(2)
    clear()    