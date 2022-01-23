# Reference from: https://www.w3schools.com/python/python_variables_global.asp
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Pyhton is " + x)
myfunc()
print("Python is " + x)

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

# Reference from: https://www.w3schools.com/python/exercise.asp?filename=exercise_lists2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)

# Reference: https://www.w3schools.com/python/python_lists_access.asp
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# Reference from: https://www.w3schools.com/python/python_lists_change.asp
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Reference from: https://www.w3schools.com/python/python_lists_add.asp
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Reference from: https://www.w3schools.com/python/python_lists_remove.asp
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Reference from: https://www.w3schools.com/python/python_lists_loop.asp
thislist = ["apple", "banana", "cherry"]
for i in thislist:
    print(i)

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Reference from: https://www.w3schools.com/python/python_lists_comprehension.asp
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for i in fruits:
    if "a" in i:
        newlist.append(i)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [i for i in fruits if "a" in i]
print(newlist)

# Reference from: https://www.w3schools.com/python/python_lists_sort.asp
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

# Reference from: https://www.w3schools.com/python/python_lists_join.asp
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1 = list1 + list2
print(list1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for i in list2:
    list1.append(i)
print(list1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# Reference from: https://www.w3schools.com/python/exercise.asp?filename=exercise_lists8
# Return the number of items in a list:
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

# Reference from: https://www.w3schools.com/python/ref_list_count.asp
# Returns the number of elements with the specified value:
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
print(points.count(9))

# Reference from: https://www.w3schools.com/python/python_dictionaries.asp
thisdict = {"brand": "Ford", "electric": False, "year": 1964, "colors": ["red", "white", "blue"]}
print(thisdict)

# Reference from: https://www.w3schools.com/python/python_dictionaries_access.asp
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict.get("model")
print(x)

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()
print(x)  # before the change
car["color"] = "white"
print(x)  # after the change

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.values()
print(x)  # before the change
car["color"] = "red"
print(x)  # after the change

# Reference from: https://www.w3schools.com/python/python_dictionaries_change.asp
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"year": 2020})
print(thisdict)

# Reference from: https://www.w3schools.com/python/python_dictionaries_add.asp
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"color": "red"})
print(thisdict)

# Reference from: https://www.w3schools.com/python/python_dictionaries_remove.asp
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)

# Reference from: https://www.w3schools.com/python/python_dictionaries_loop.asp
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in thisdict:
    print(x)
for x in thisdict.keys():
    print(x)
for x in thisdict.values():
    print(x)

# Reference from: https://www.w3schools.com/python/python_dictionaries_nested.asp
child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}
child3 = {"name": "Linus", "year": 2011}
myfamily = {"child1": child1, "child2": child2, "child3": child3}
print(myfamily)

# Reference from: https://www.w3schools.com/python/python_conditions.asp
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Reference from: https://www.w3schools.com/python/python_while_loops.asp
i = 1
while i < 6:
    print(i)
    i = i + 1

# Reference from: https://www.w3schools.com/python/python_for_loops.asp
for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

for i in range(2, 6):
    print(i)

for x in range(7, 21, 3):
    print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# Reference from: https://www.w3schools.com/python/python_functions.asp
def function():
    print("A function is a block of code which only runs when it is called.")
function()

def function(first_name, last_name):
    print(first_name + " " + last_name)
function("Steve", "Jobs")

def my_function(child1, child2, child3):
    print("The youngest child is " + child3)
my_function(child1="Ashley", child2="Katherine", child3="Ryan")

def function(food):
    for i in food:
        print(i)
food = ["bread", "egg", "milk"]
function(food)

def my_function(x):
    return 5 * x
print(my_function(4))
print(my_function(6))
print(my_function(8))

# Reference from: https://www.w3schools.com/python/python_lambda.asp
x = lambda a : a + 5
print(x(5))

y = lambda b, c : b * c
print(y(4, 9))

z = lambda d, e, f : d + e / f
print(z(5, 9, 3))

# Reference from: https://www.w3schools.com/python/python_arrays.asp
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

# Reference from: https://www.w3schools.com/python/python_datetime.asp
import datetime
x = datetime.datetime.now()
print(x)

import datetime
x = datetime.datetime(2022, 1, 12)
print(x)

# Reference from: https://www.w3schools.com/python/python_math.asp
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

x = abs(-12.5)
print(x)

x = pow(6, 3)
print(x)

import math
x = math.sqrt(64)
print(x)

import math
x = math.ceil(9.8)
y = math.floor(9.8)
print(x) # returns 10
print(y) # returns 9

import math
x = math.pi * pow(4, 2) # Circle area with a radius of 4
print(x)