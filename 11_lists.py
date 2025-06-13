"""
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
"""

"""
#Ordered

When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.
"""


"""
Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
"""


# nameList = ["muhammad", "Mehedi", "Hasan", "Hasan"]
# print(nameList)
# print(type(nameList))


# gibrish_list = ["hasan", True, 100, ["another", "list", "inside"]]
# print(gibrish_list)


# another_tyeOf_list = list(("is't", "a", "list", "too!"))
# print(another_tyeOf_list)

# nameList[3] =  "i am unstopable, fire!"
# print(nameList)


# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[0:3])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["lichi", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")
# else:
#   print("No, 'apple' is not here!")


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = "blackcurrant", "watermelon"
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = "blackcurrant", "watermelon"
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(0, "watermelon")
# print(thislist)


# name = ["muhammad", "mehedi"]
# name.append("hasan")
# print(name)

# name_fisrt = ["muhammad", "hasan"]
# name_last = ["mehedi"]
# name_fisrt.extend(name_last)
# print(name_fisrt)

# name_fisrt = ["muhammad", "mehedi"]
# name_dict = {"lastname": "hasan"}
# name_fisrt.extend(name_dict)
# print(name_fisrt)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# name = ["muhammad", "mehedi", "hasan"]
# del name[2]
# print(name)

# name = ["muhammad", "mehedi", "hasan"]
# del name    #deletes the entire list
# # print(name)  #as the list is deleted, it shows NameError: name 'name' is not defined

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]


# name1 = ['mehediXD', 'hasanXD', 'not found!', 'h-XD']
# name2 = []
# for _ in name1:
#   if 'h' in _:
#     name2.append(_)
# print(name2)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newListOfFruits = [x for x in fruits if "a" in x]
# print(newListOfFruits)
# newListOfFruits = [x for x in fruits if x != "apple"]
# print(newListOfFruits)
# newListOfFruits = [x for x in fruits]
# print(newListOfFruits)
# newListOfFruits = [x for x in range(5)]
# print(newListOfFruits)
# newListOfFruits = [x for x in range(10) if x <= 5]
# print(newListOfFruits)
# newListOfFruits = [x.upper() for x in fruits]
# print(newListOfFruits)
# newListOfFruits = ['changed!' for x in fruits]
# print(newListOfFruits)
# newListOfFruits = [x if x != "banana" else "orange" for x in fruits]
# print(newListOfFruits)


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)
# thislist.sort(reverse=True)
# print(thislist)


# def myfunc(n):
#   return abs(n - 1)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["banana", "Zorange", "kiwi", "cherry"]
# thislist.sort()
# print(thislist)



# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)


# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)