"""Exception Handling"""

# x = 10
# try:
#     print(x)
# except:
#     print("An exception occurred")


"""Many Exceptions"""

# x = 10
# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("Something else went wrong")


"""Else BLOCK"""
# x = 10
# try:
#     print(x)
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")


"""Finally BLOCK"""

# x = 10
# try:
#     print(x)
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")
# finally:
#     print("This will print no matter what!")


"""EXAMPLE"""

# try:
#     f = open("demofile.txt", "w")
#     try:
#         f.write("Lorum Ipsum - Lorum Ipsum - Lorum Ipsum - Lorum Ipsum")
#         print(
#             "\n\n'Lorum Ipsum - Lorum Ipsum - Lorum Ipsum - Lorum Ipsum' was written down to the demofile, check it!\n\n"
#         )
#     except:
#         print("Something went wrong when writing to the file")
#     finally:
#         f.close()
# except:
#     print("Something went wrong when opening the file")


# x = -1

# if x < 0:
#     raise Exception("Sorry, no numbers below zero")


# x = "hello"

# if not type(x) is int:
#     raise TypeError("Only integers are allowed")
# else:
#     print("You're good to go")


x = input("Enter any value: ")

if x < 5 or x > 9:
    raise ValueError("Value shoould be between 5 and 9!")
elif x == "quit":
    print("quited!")
else:
    print("You'r good to go")
