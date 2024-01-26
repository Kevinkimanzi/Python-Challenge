# Exception handling - events detect during execution that interrupt the flow of a program 
# a number divide by zero will generate an error


try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide: "))
    result = numerator / denominator
    print (result)
except Exception:
    print("Something went wrong: ")

# Its good practice to have several exceptional blocks

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide: "))
    result = numerator / denominator
    print (result)
except ZeroDivisionError:
    print("You cannot divide by zero! Idiot!")
except ValueError:
    print("Enter only numbers please!")

except Exception:
    print("Something went wrong: ")
else:
    print(result)
finally:
    print("This will always execute")


## FILE DETECTION
    
# Check if path exists and whether it is a file
# EXAMPLE 1
    
import os
path = "//home/kevin//kevin//Python-Challenge//file-detection.txt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("This is a file")
    if os.path.isdir(path):
        print("This is a directory")
else:
    print("That location doesn't exist")

# EXAMPLE2

import os
path = "//home/kevin//kevin//Python-Challenge"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("This is a file")
    if os.path.isdir(path):
        print("This is a directory")
else:
    print("That location doesn't exist")

