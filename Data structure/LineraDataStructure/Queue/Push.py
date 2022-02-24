
    # def enqueueCharacter(self,element):
    #     return self.s.append(element)
    
    # def dequeueCharacter(self):
    #     return self.s.pop(0)
#FIFO

class Queue:
    def __init__(self) -> None:
        self.data=[]
    
    def enqueue(self,element):
        if len(self.data)==5:
            print("Overflow")
        else:
            self.data.append(element)
    
    def dequeue(self):
        if len(self.data)==0:
            print("Underflow")
        else:
            self.data.pop(0)
    
q=Queue()
q.enqueue(1)
q.enqueue(2)
print(q.data)
q.dequeue()
print(q.data)
