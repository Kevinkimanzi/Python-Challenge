# FUNCTION - a block of code which is executed only when it is called

def hello(name):
    print("Hello! "+name)
    print("Have a nice day!")
my_name = "KIM KIM"
hello("Kevin")
hello(my_name)


def hello(name, age, height):
    print("Hello! "+name+ " "+ str(age)+ " "+str(height))
    print("Have a nice day!")

hello("Kevin", 21, 20)

# RETURN STATEMENT -functions send python values/objects back to the caller
#                   These values are known as function return values

def multiply (number1, number2):
    result = number1 * number2
    return result

x = multiply(6, 8)

print(x)


# KEYWORD ARGUMENT - Argument preceded by an identifier when we pass them to a function

def hello(first, middle, last):
    print("Hello "+first+ " "+middle+" "+last)

hello(middle="Kimanzi",last="Kilonzi",first="Kevin")


#NESTED FUNCTION - Functions calls inside other function calls
#                - inner most function are resolved first

print(round(abs(float(input("Enter a whole number: ")))))
