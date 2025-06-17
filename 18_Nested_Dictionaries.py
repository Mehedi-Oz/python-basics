family = [
    {"person1": "PERSON1", "year": 90523},
    {"person2": "PERSON2", "year": 343534264},
    {"person3": "PERSON3", "year": 23423},
]

print(type(family))
print(family)

family = {
    "Person-01": {"name": "amigos-1", "year": 1},
    "Person-02": {"name": "amigos-2", "year": 2},
    "Person-03": {"name": "amigos-3", "year": 3},
}

print(type(family))
print(family)

for x, obj in family.items():
    print("x", x)

    for y, z in obj.items():
        print( y, z)

print(family["Person-01"]["name"])