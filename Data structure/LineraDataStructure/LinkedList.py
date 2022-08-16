class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution: 
    def display(self,head):
        '''display method will traverse through linked list and display each data in it'''

        current = head  # current points to head

        while current:  # checking if current is pointing to None or not
            print(current.data,end=' ')
            current = current.next  # current is now pointing to next node

    def insert(self,head,data): 
        '''Insert method used to creating new data 
            to existing data'''
            
        temp = Node(data)   # creating new node
        if head is None:    # this block of code is executed only once in the whole life of the program
                            # checks if head is pointing to None or not
            head = temp     # now created head points to new node
            return head     
        
        # if the above if condition goes False interpreter comes below 
        current = head      # now head points to current
        while current.next is not None:     # checking if the current's next is not None
            current = current.next    
        current.next = temp     # current.next is now pointing to newly created node
        return head 

mylist= Solution()
# T=int(input("Enter the nodes you want to Insert: "))
T = 3
head=None
data=1
for i in range(T):
    head=mylist.insert(head,data)  
    data=data+1 
mylist.display(head)


# l=[1,2,3]
# # print(l.__len__())
# # print(dir(l))

# di = {'a':1, 'b':2}
# # print(dir(di))

