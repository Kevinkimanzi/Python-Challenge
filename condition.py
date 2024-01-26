# if statement = block of code that will execute if the condition is true

age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult")
elif age < 0:
    print("You havent been born!")
else:
    print("You are a Child")


# logical operators - used to check if 2 or more statement is true
# and, or, not
    
temp =int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today")
    print("Go outside!")
elif temp < 0 or temp > 30:
    print ("The temperature is bad today!")
    print ("Stay inside!")

#While loop - will execute its block of code as long as its condition remain true

name = ""
while len(name) == 0:
    name =  input("Enter your name: ")
    print("Hello "+name)

#For Loop - will execute it's block of code a limited number of time
# while loop - unlimited

#count down timer
    
for i in range(10):
    print(i+1)

    
