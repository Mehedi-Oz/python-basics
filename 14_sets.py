"""
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values
"""

thisset = {"apple", "banana", "cherry"}
print(thisset)


"""
The values True and 1 are considered the same value in sets, and are treated as duplicates
"""


thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)


"""
The values False and 0 are considered the same value in sets, and are treated as duplicates
"""
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)


thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add("newItem")
print(thisset)

thisset = {"apple", "banana", "cherry"}
newset = {"_"}
thisset.update(newset)
print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


"""
Note: If the item to remove does not exist, remove() will raise an error
"""

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


"""
Note: If the item to remove does not exist, discard() will NOT raise an error
"""

thisset = {"apple", "banana", "cherry"}
thisset.discard("banaynay")
print(thisset)


thisset = {"apple", "banana", "cherry"}
print(thisset.pop())


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
for _ in thisset:
  print(_)