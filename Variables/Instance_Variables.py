class Instance:
    def __init__(self, x) -> None:
        """Instance variables are those memory will be 
        allocated only once when object of the class is created"""
        self.x=x
    
    def modify(self):
        """when we modify any instance variables it doesn't change
        in object objects. It's independent variable"""
        self.x+=1
    
o1 = Instance(1)
o2 = Instance(1)

print(o1.x, o2.x)

o1.modify()

print(o1.x, o2.x)