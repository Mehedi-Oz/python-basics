# x = 15
# y = 4

# print("Floor division ", x // y)  # Floor division

# x, y = 8, 2

# print("Bitwise Left ", x << y)  # Bitwise Left

# print("Bitwise Right ", x >> y)  # Bitwise Right

# print("Bitwise AND ", x & y)  # Bitwise AND
# """
#   Bit Position:  3 2 1 0 
#   x (1000):      1 0 0 0  
#   y (0010):      0 0 1 0  
#   ----------------------    # Bitwise AND
#   Result (x&y):  0 0 0 0  
# """

# x, y = 8, 2
# print("Bitwise XOR ", x ^ y)  # Bitwise XOR
# """ 
#   Bit Position:  3 2 1 0
#   x (1000):      1 0 0 0
#   y (0010):      0 0 1 0
#   ----------------------   #Bitwise XOR (if both are different then 1, if similar then 0)
#   Result (x^y):  1 0 1 0
# """

x, y = 8, 2
print("Bitwise OR ", x | y)  # Bitwise OR
""" 
  Bit Position:  3 2 1 0
  x (1000):      1 0 0 0
  y (0010):      0 0 1 0
  ----------------------   #Bitwise OR (if both are 0 then 0, else 1)
  Result (x^y):  1 0 1 0
"""
