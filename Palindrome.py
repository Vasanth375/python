#copy is python library used to perform copy operations
import copy as cp

#string input
a=123212

a=str(a)
#converting it into list
a=list(a)

#coping the list a to b
b=cp.copy(a)

#reversing a object according to palindrome theory revering of an object the same object seems like previous object
b.reverse()

#just converting list into str
b="".join(b)
a="".join(a)

print(True if a==b else False)