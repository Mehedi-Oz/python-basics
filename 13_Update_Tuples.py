# x = ("apple", "banana", "cherry")
# print(type(x), x)

# y = list(x)
# print(type(y), y)

# new_item = "newfruit"
# y.append(new_item)
# print(type(y), y)

# x = tuple(y)
# print(type(x), x)

# new_tuple = ("newTuple?",)
# x += new_tuple
# print(x)




"""
Python - Unpack Tuples
"""

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)


#Using Asterisk*

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print("Using Asterisk*")
# print(green)
# print(yellow)
# print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)



"""Multiply Tuples"""


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)