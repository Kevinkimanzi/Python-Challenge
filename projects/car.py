# OPP
#  __init__ method in Python is used to initialize objects of a class. It is also called a constructor


class Car:


    wheel = 4     #setting default number of wheels for car1 and 2
    
    def __init__(self, make, model, year, color):
        self.make = make   #instance variable
        self.model = model  #instance variable
        self.year = year     #instance variable
        self.color = color  #instance variable

    def drive(self):
        print("This " +self.model+ " "+" is driving")

    def stop(self):
        print("This " +self.model+ " "+" is Stopping")

        
# Inheritance in python
# Classes can inherit something..classes can have children
    

class Animal:

    alive = True

    def eat (self):
        print("This Animal is Eating")

    def sleep (self):
        print("This Animal is Sleeping")


class Rabbit (Animal):
    pass

class Fish (Animal):
    pass

class Goat (Animal):
    pass

rabbit = Rabbit()
fish = Fish()
goat = Goat()

print(rabbit.alive)
fish.eat
goat.sleep

# Multi level inheritance - when a derived child class inherit from another derived child
#  class

class Organism:

    alive = True

class Animals(Organism):
    def eat (self):
        print("This Animal is Eating")

class Dog(Animals):

    def bark (self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()

##METHOD CHAINING

class Cars:

    def turn_on(self):
        print("You start the Engine")
        return self
    
    def drive(self):
        print("You drive the car")
        return self

    
    def brake(self):
        print("You step on the  brakes")
        return self

    
    def turn_off(self):
        print("You turn_off the Engine")
        return self


car = Cars()
car.turn_on().drive()

car.turn_on().drive().brake().turn_off()

# Super function = Ruturn a temporally object of a parent class when used
"""
class Rectangle:
    pass

class square(Rectangle):
    def __init__(self, length, width):
        self.length = length
        self.width = width

class cube(Rectangle):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

square(3,3)
cube(3,3,3,)
print(square)
"""
    ## WE ARE REPEATING SOME CODES LIKE 
"""def __init__(self, length, width):
        self.length = length
        self.width = width""" # THEREFORE WE CAN REUSE

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    
    def area(self):
        return self.length*self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height

square = Square(3,3)
cube = Cube(3,3,3,)

print(square.area())
print(cube.volume())


## ABSTRACT CLASS - PREVENT USER FROM CRAETING OBJECT OF THAT CLASS



