class Class_Variables:
    x=1

    @classmethod
    def modify(self):
        self.x+=1
        

c1 = Class_Variables()
c2 = Class_Variables()

print(c1.x, c2.x)

c1.modify()

print(c1.x, c2.x)
