# # x = "awesome"

# # def myfunc():
# #   global x
# #   x = "fantastic"

# # myfunc()

# # print("Python is " + x)


# x = 1j
# c1 = complex(3, 4)
# c2 = complex(5)
# c3 = complex()
# print(x, c1, c2, c3)

# # Accessing real parts
# print(c1.real)

# # Accessing imaginary parts
# print(c1.imag)

# print(c1 + c2)


# x = range(-1)
# print(x)


# x = b"Hello"
# print(x)

# x = bytearray(1)
# print(x)

# x = memoryview(bytes(5))
# print(x)

# x = None
# print(x)

# x = bytes(5)
# print(x)

# import random

# print(random.randrange(1, 5))

# name = 'don\'t do it! "Oh my god!"'
# print(name)

# a = "Hello, World!"
# print(len(a))

# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# txt = "The best things in life are free!"
# if "best" not in txt:
#     print("No, 'expensive' is NOT present.")
# else:
#     print("its here!")


# b = "Hello, World!"
# print(b[2:100000000])


# a = "Hello, World!"
# print(a.upper())

# a = " Hello, World! "
# print(a.strip())


# a = "Hello"
# b = "World"
# c = a + b
# print(c)


# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)


# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# backSlash = "here is a\r backslash"
# print(backSlash)


# txt = "Hello, And Welcome To My World!"
# x = txt.casefold()
# print(x)


# print(bool("Hello"))
# print(bool(["apple", "cherry", "banana"]))

thisDict = {
    "name": "hasan",
    "model": "Ryzen",
    "year": 2025,
}

print(thisDict)


x = thisDict["model"]
print(x)

x = thisDict.get("year")
print(x)

keys = thisDict.keys()
print(keys)


car = {"brand": "Ford", "model": "Mustang", "year": 1964}

car["color"] = "gray"
print(car)

print(car.values())

print(car.items())

car.update({"model": "supra"})

print(car)

# car.pop("year")
car.popitem()
print(car)


car = {"brand": "Ford", "model": "Supra", "year": 1964}
del car["year"]
print(car)


car = {"brand": "Ford", "model": "Supra", "year": 1964}
car.clear()
print(car)


car = {"brand": "Ford", "model": "Supra", "year": 1964}
for x, y in car.items():
  print(x, y)

