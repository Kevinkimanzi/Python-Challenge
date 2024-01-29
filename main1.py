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
# Check if path exists and whether it is a directory
    
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


# READ AND WRITE A FILE
# will close file after opening it
    
with open('test.txt') as file:
    print(file.read())

print(file.closed)  #checking is the file was closed

# Assume I made error typing my file name
try:
    with open('test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found" )

## WRITING A FILE
#This will overwrite my test.txt
    
test = "YOOOH! This is a test\nhave a good one"
with open('test.txt','w') as file:
    file.write(test)

# To append a file instead of overwritting

test = "Please append this one"
with open('test.txt','a') as file:
    file.write(test)

# COPY A FILE
# copyfile() = copy content of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copy metadata
    
import shutil

shutil.copyfile('test.txt', 'copy.txt') #file copied to my project

## MOVING FILES 
#Move file from project to destination

import os
source ="test.txt"
destination = "//home/kevin//kevin//test-moved.txt"

try:
    if os.path.exists(destination):
        print("There is a file there")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print("sorce file not found")

# deleting a file
    
import os
path ="copy.txt"
try:
    os.remove(path)
except PermissionError:
    print("File was not found")



## Modules - a file containing python codes. may contain funcion, classes etc
# assume we have another file called modules.py with functions

import modules as mdl

mdl.hello()
mdl.bye()

# OR
from modules import hello