# strings are immutable

a = "Hasan"
print(len(a))
print(a.upper())
print(a.lower())

b = "!!!!!!!!!!! HASAN !!!!!!!!!!!"
print(b.rstrip("!"))
print(b.replace("!!!!!!!!!!!", "XXX"))
print(b.split(" "))

blog = "i can do this!"
print(blog.capitalize())

blog = "i can do This, i can do that!"
print(blog.center(50))

print(blog.count("do"))

print(blog.endswith("that!"))

print(blog.endswith("do", 1, 8))

blog = "i can do This, i can do that!"
print(blog.find("This"))

print(blog.find("dos"))
print(blog.index("do"))

blog = "12234dgsfd"
print(
    blog.isalnum()
)  # returns true A-Z, a-z, 0-9, false if special characters are included

blog = "hello"
print(blog.isalpha())  # returns true if all are letters, false if numbers are included

print(blog.islower())


printable = "is this a           printable variable!"
print(printable)
print(printable.isprintable())

whitespace = "          "
print(whitespace.isspace())


blog = "i can do This, i can do that!"
print(blog.istitle())
print(blog.title())

blog = "i can do This, i can do that!"
print(blog.istitle())
print(blog.title())

print(blog.startswith("i can"))

print(blog.swapcase())


x = "abc"
def check():
    x = "bcd"
    print(f"x is {x}")
check()
print(x)


