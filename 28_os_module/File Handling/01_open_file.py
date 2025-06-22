"""Python File Open"""

import os

openFile = open("textfile.txt")
print("\n\n", openFile.read(), "\n\n")
openFile.close()

"""Using the with statement"""

with open("textfile.txt") as openFile:
    print(openFile.read())


"""Read Only Parts of the File"""

with open("textfile.txt") as f:
    print(f.read(5))


with open("textfile.txt") as f:
    print(f.readline())


with open("textfile.txt") as f:
    for x in f:
        print(x)
