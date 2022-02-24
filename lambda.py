a=lambda x,y:x+y
print(a(19,19))
'''
inside operation of lambda function
lambda(a)
{return a+1}
'''

def myfun(v):
    return lambda u:u+v

z=myfun(10)
print(z(5))
'''
inside of this is
z(5) means u value is 5
myfun(10) means v value 10
'''