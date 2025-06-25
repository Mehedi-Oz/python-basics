x = 10


def check_num():
    x = 11
    print("local x: ", x)
    y = 10


check_num()
print("global x: ", x)
print(y)
