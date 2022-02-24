''' Constructor is function that is called when a instance of a class is defined or created.
    like java python doesn't support multiple constructors in use.
    python support two types of constructors
    1)Default constructor.
    2)parameterized constructor'''
# 1) Default constrctor example
class bike:
    def __init__(self) -> None:
        print("hello world")

b=bike()

# 2)Parameterized constructor example
class car:
    def __init__(self,h,w) -> None:
        print("Car Name:",h)
        print("Model Num:",w)
        
c=car("Volvo",4356)
