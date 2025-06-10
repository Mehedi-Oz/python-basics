name = "Hasan"

big_string = """This is a big string
Next Line!
Another Line!"""

print(big_string)


print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) #IndexError: string index out of range

for character in big_string:
    print(character)
