# Arrays are used to store multiple values in one single variable:

cars = ["Ford", "Volvo", "BMW"]

for car in cars:
    print(car)

print(cars[0])

print("The Length of an Array")

x = len(cars)
print(x)

print('Adding Array Elements')
cars.append("Honda")

for eachCar in cars:
    print(eachCar)

print('Removing Array Elements')
cars.pop(3)

for car in cars:
    print(car)

print('You can also use the remove() method to remove an element from the array.')

cars.remove("Volvo")

print(cars)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
