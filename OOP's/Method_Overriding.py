#if we had situation like same method same in both classes
class A:
    def printf(self):
        print("Baseclass")

    def add(self):
        print("Nope")
class B(A):
    def printf(self):
        print("this is subclass")
    def add(self):
        print("NopeB")

b=B()
b.printf()
b.add()
