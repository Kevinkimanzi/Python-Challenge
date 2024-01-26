# list stores multiple items in a single variable

food = ["pizza", "hamburger", "hotdog"]
print(food)
print(food[2])

# to add
food.append("meat")

# to remove
food.remove("pizza")

#display all element

for i in food:
    print(i)

# 2D LIST
drinks = ["coffe","soda","tea"]
food = ["pizza", "hamburger", "hotdog"]
desssert = ["cake","icecream"]

meal = [drinks,food,desssert]

print (meal)

# tuple = collection which is ordered and unchangedable used to group together related data

student = ("kevin", 21, "male")
print(student.count("kevin"))

for x in student:
    print(x)

if "kevin" in student:
    print("Kevin is here!")

# SET - Collection which is unordered, unindexed. no duplicated values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}

diner_table = utensils.union(dishes)
print(diner_table)

for x in diner_table:
    print(x)

# Distionary- a changeable, unordered collection of unique key:value pairs
#  Fast bacause they use hashing

capitals = {'USA':'washington',
            'India':'New Deli',
            'Kenya':'Nairobi',
            'China':'Beijin',
            'Russia':'Moscow'}

print (capitals["Russia"])
print(capitals.get("Germany"))

# to add key

capitals.update({"Germany":"Berlin"})

# print country and capital
for key, value in capitals.items():
    print(key, value)

# INDEX OPERATOR [] = Gives access to a sequence's element (str, list, tuples)
name = "Kevin Kimanzi"

if(name[0].islower()):
    name = name.upper()
    print(name)




