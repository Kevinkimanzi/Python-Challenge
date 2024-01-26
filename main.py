# variable = a container for a value
#string
first_name = "Kevin "
second_name = "Kimanzi"
last_name = "Kilonzi"
full_name = first_name + " "+ second_name +" "+last_name

print("Hello " +full_name)

#integer
age = 21
age += 1

print (age)

# print name alongside age
#can only concatenate str (not "int") to str

print("Your age is" +" " +full_name +" " +str(age))

#FLOAT
height = 100.5 
print ("you are of" +" " +str(height) +" " +"of height")

#boolean

human = False

print ("Are you a human:" +" " +str(human))

#Multiple assignment 
# -allow us to assign multiple variable

name, age, height = "Kevin Kimanzi", 22, 100.5

kevin =karis = leah = 30
print(kevin)
print(name)

# STRING METHODS

print(len(name))

#capitalize first letter
print(name.capitalize())

#uppercase and lowercase
print(name.upper())
print(name.lower())

#TYPE CASTING
# Ability to convert a data type of a value to another data type

x = 1 
y = 20.5
z = "3"
x= float(x)
y= int(y)
print(type(y))
print(y*4)
print(x)

# USER INPUT
name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))
age +=1
print("Hello " +name +" " +"You are " +str(age) +" "+"old" +" "+"and" +" " +str(height) +"cm tall")

#ARGS AND KWARGS

# ARGS - Parameter that will pack all argumnets into a tuple

def add(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum

print(add(1,2,3,4,5))

# kwags - parameter that will pack all argument into a dictionary
#         useful so that a function can accept a varying amount of keyword argument

def hello(**kwargs):
    print("hello "+ kwargs['first']+ " "+kwargs['last'])

hello(first="kevin", middle="kimanzi", last = "KIlonzi")


#String.format() - optional method that gives user 
#                 more control when displaying output

animal = "cow"
item = "moon"
name = "Kevin"
 #lets print the cow jumped over the moon

print ("The {} jumped over the {}".format("cow","moon"))
# or
print ("The {} jumped over the {}".format(animal,item))

text = "The {} jumped over the {}"
print(text.format(animal,item))

print("Hello, my name is {}".format(name))

## Formating number
# display 2 digit after the decimal

number = 3.14159

print("The number pi is {:.2f}".format(number))

