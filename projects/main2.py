"""
from car import Car

car_1 = Car ("Toyata", "Vits", 2015, "White")
car_2 = Car ("ford", "Ranger", 2015, "White")


print (car_1.make)
print (car_1.model)
print (car_1.year)
print (car_1.color)

car_2.drive()
car_1.stop()"""

# lambda Function - written in 1 line and are written using lambda keyword
"""
def double (x):
    return x * 2
"""
# same as
double = lambda x:x * 2
multiply = lambda x, y: x * y
add = lambda x,y, z: x + y + z
full_name = lambda first, last : first + " " + last
print(double(100))
print(multiply(5,6))
print(full_name("kevin", "Kimanzi"))
print(add(5,6, 8))

age_check = lambda age:True if age >= 18 else false

# SORT ITERABLES
student = ["kevin", "alex", "brian", "leah"]

student.sort()
for i in student:
    print(i)
student.sort(reverse = True)
for i in student:
    print(i)

## Zip function: aggregate element drom two or more itereble(list, tuples,set, etc)
    
username  = ["kev", "kim", "kil"]
password = ("kaka"," gdgeg", "hsdshd")

users = zip(username, password)
for i in users:
    print(i)
    # output
"""  ('kev', 'kaka')
    ('kim', ' gdgeg')
    ('kil', 'hsdshd') """


# if __name__ = '__main__'

