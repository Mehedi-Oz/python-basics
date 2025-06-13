thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

print(thisdict)


"""
Duplicates Not Allowed
Dictionaries cannot have two items with the same key
"""
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
print(thisdict)


thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}
print(thisdict)


"""
The dict() Constructor
"""

thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)


