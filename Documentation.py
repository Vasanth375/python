# # when some statements of comments written inside of function that is called documentation of that function
# # we can perform this in class also etc.
# def add():
#     '''add function gives us add operation'''
#     print(1+4)

# add()
# print(add.__doc__)


from random import randint
t=int(input())
for i in range(t):
    li=list(input())
    a=li[0]
    b=li[1]
    m=0
    while(a != b):
        a=a+1
        b=b+1
        n=randint(1,50)
        m=m+1
        a=a or n
    print(m)
