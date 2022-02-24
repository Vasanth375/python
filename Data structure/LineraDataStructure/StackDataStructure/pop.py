class Stack:
    def __init__(self,n):
        self.data,self.n=[],n
    
    #push function
    def push(self,element):
        if len(self.data)<self.n:
            self.data.append(element)
        else:
            print("Overflow")
    #pop function 
    def pop(self):
        if len(self.data)==0:
            print("Undreflow")
        else:
            self.data.pop()

st=Stack(5) #passing length of list in to constructor

#pushing element to stack
for i in range(5):
    st.push(i+1)
print(st.data)

#poping elements to stack
for i in range(6):
    st.pop()
