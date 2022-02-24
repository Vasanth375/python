# logical or bitwise operators

# 0 - False, less than zero or more than zero is True
# -2,-1,1,2 - True

a=5
b=6
print(bool(a))
print(bool(b))
print(bool(a) or bool(b))
# or operator will return true if any of either is true
print(a or b)
# and operator will return true if both were true
print(a and b)
# this will return false if operand is true
print(not a)