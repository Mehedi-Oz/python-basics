"""
"x" - Create - will create a file, returns an error if the file exists
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"""

with open("textfile.txt", "a") as f:
    f.write("\n\nThis is a new line, added from write file\n\n")

with open("textfile.txt") as f:
    print("\n\n", f.read(), "\n\n")


with open("textfile.txt", "w") as f:
    f.write(
        "Previous texts are gone beacause of 'w'\n\nThis is a new line, added from write file\n\n"
    )

with open("textfile.txt") as f:
    print("\n\n", f.read(), "\n\n")


with open("newfile.txt", "x") as n:
    open("newfile.txt", "w")
    n.write("This is a new file!")
