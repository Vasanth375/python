'''object are instance of the classes, that means memory allocated by the interpreter and that memory space name 
    is identifier used to create object '''
class Arithmetic:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    def Add(self):
        '''Addition function'''
        c=self.a+self.b
        print(c)

Arith = Arithmetic() #creating object for Arithmetic class to Add a+b
Arith.Add()
