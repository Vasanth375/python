import random

a=list(range(10))

#Creating random 10 digits number
num=[str(random.choice(a)) for i in range(10)]

#Displaying it
print("".join(num))
