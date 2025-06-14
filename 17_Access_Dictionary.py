thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict["model"]
print(x)


thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict.get("model")
print(x)


thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict.keys()
print(x)


car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.keys()
print(x)  # before the change

car["color"] = "white"
print(x)  # after the change

x = thisdict.values()
print(x)

x = thisdict.items()
print(x)


car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.items()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change


newDict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}
print(newDict)

print(newDict.get("key3"))

print(newDict.keys())
print(newDict.items())
print(newDict.values())


newDict["key4"] = "value4"
print(newDict)


newDict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}

for _ in newDict.values():
    print(f"Current key: {_}")
    if "value3" in _:
        print("gotcha!")
    else:
        print("sorry boss!")


thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"year": 2020})
print(thisdict)


newDict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}
# newDict.pop("key2")
thisdict.popitem()
print(newDict)
