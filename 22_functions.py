def whatsMyName():
    print("Hasan")


whatsMyName()


def adding_numbers(x, y):
    y = x + y
    print(y)


adding_numbers(11, 22)


def my_function(*kids):
    print("The youngest child is " + kids[0])


my_function("Emil", "Tobias", "Linus")


def my_function(**names):
    print("My first name is ", names["fname"])


my_function(fname="mehedi", lname="hasan")


def my_names(names):
    for _ in names:
        print(_)


names = ["muhammad", "mehedi", "hasan"]
my_names(names)


def my_function(x, /):
    print(x)


my_function(3)


def mixed_function(a, /, b, *, c):
    # 'a' is positional-only
    # 'b' can be positional or keyword
    # 'c' is keyword-only (due to the '*' separator)
    print(f"a: {a}, b: {b}, c: {c}")


# Valid calls:
mixed_function(10, 20, c=30)  # a=10 (pos), b=20 (pos), c=30 (kw)
mixed_function(10, b=20, c=30)  # a=10 (pos), b=20 (kw), c=30 (kw)

# Invalid calls:
# mixed_function(a=10, b=20, c=30) # TypeError: a is positional-only
# mixed_function(10, 20, 30)       # TypeError: c is keyword-only
