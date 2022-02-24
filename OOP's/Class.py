'''
Simula is the first object oriented programming language. It was developed by 1967
Object-Oriented Programming(OOP), is all about creating “objects”. An object is a group 
of interrelated variables and functions. These variables are often referred to as properties 
of the object and functions are referred to as the behavior of the objects.
OOP's Concepts
Class
Object
Method
Inheritance
Encapsulation
Polymorphism
Data Abstraction
'''
'''
Class:
Class is a collection of objects
'''
#class Documentation
# print(numpy.__doc__)
class HelloWorld:
    world="World"
    def Add(self,w):
        print("hello",w) #self is just a reference to the HelloWorld class attributes

N=HelloWorld() #creating object to HelloWorld class
N.Add('World') #calling the function 
