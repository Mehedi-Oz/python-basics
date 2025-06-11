# value = int(input("Enter a value: "))

# match value:
#     case 0:
#         print("value is 0!")
#     case 1:
#         print("value is 1")
#     case 100:
#         print("value is 100")
#     case _ if value != 10:
#         print(value)
#     case _ if value != 20:
#         print(value, "is not 20")
#     case _ : 
#       print("value is ", value)

month = 6
day = 31
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")