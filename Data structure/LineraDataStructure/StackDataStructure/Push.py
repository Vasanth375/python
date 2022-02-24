class Stack:
    def __init__(self,n) -> None:
        self.data,self.n=[],n
    
    def push(self,element):
        if len(self.data)<self.n:
            self.data.append(element)
        else:
            print("Overflow")

    def is_full(self):
        if len(self.data)==self.n:
            return True
        else:
            return False

st=Stack(5) #passing length of list in to constructor
for i in range(5):
    st.push(i+1)
print(st.data)

print(st.is_full())
#returns true if stack is full 