# list ordered and mutable
# datastructures
mylist = ["Jose", "Luka", "Mercy", "Daniel", "Gloriah", "Brian"]
mylist2 = [65, 43, 5, -5, -8, 45, 74, 28, 13, 95]
mylist2.sort()
mylist2.extend([2, 5, 9])
mylist.insert(3, "Margaret")
mylist.sort()
mylist.append("John")
print(mylist)
print(f"My name is {mylist[1]}")
print("My name is", mylist[1])
print(f"My sorted list is {mylist2}")

# tuple immutable
my_tuple = ("Kenya", "Uganda", ["Usa", "Russia", "Israel"], "Tanzania", " Ethiopia")
print(my_tuple)
print(f"My country is {my_tuple[0]}")

# set unordered
fruits = {"Oranges", "Apples", "Mangoes", "Banana"}
print(fruits)

# Dictionaries
employees = {"Name": "Joseph", "Age": 30, "salary": 10000}
print("Employees name :%s" % employees["Name"])
print("Employees age :%d" % employees["Age"])
