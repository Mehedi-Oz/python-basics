"""
Union
The union() method returns a new set with all items from both sets
"""

set1 = {"a", "b", "c", 3}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2  # union()
print(set3)


"""
Join a Set and a Tuple
"""

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)


"""
Update
The update() method inserts all items from one set into another.
The update() changes the original set, and does not return a new set.
"""


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


"""
ntersection
Keep ONLY the duplicates
The intersection() method will return a new set, that only contains the items that are present in both sets.
"""

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)



"""
The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
"""

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)


set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)


"""
Difference
The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
"""


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)



"""
Symmetric Differences
The symmetric_difference() method will keep only the elements that are NOT present in both sets.
"""

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)