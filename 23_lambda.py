# multiply = lambda x: x * 10
# print(multiply(10))


# def myfunc(n):
#     return lambda a: a * n


# mytripler = myfunc(3)
# print(mytripler(11))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
