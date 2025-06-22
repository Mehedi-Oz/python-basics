with open("newfile.txt", "x") as n:
    open("newfile.txt", "w")
    n.write("This is a new file!")


"""Check if File exist"""

import os

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
    print("File deleted")
else:
    print("This file doesnt exist!")


"""Delete Folder"""
"""To remove a folder with the os module, it cannot contain any files"""

os.mkdir("demofolder")

if os.path.exists("demofolder"):
    os.rmdir("demofolder")
    print("Folder deleted")
else:
    print("This folder doesnt exist!")
