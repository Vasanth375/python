# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None 

# class Solution: 
#     def display(self,head):
#         current = head
#         while current:
#             print(current.data,end=' ')
#             current = current.next

#     def insert(self,head,data): 
#         temp = Node(data)
#         if head is None:
#             head = temp
#             return head
#         current = head
#         while current.next is not None:
#             current = current.next
#         current.next = temp
#         return head 

# mylist= Solution()
# T=2
# head=None
# data=1
# for i in range(T):
#     head=mylist.insert(head,data)  
#     data=data+1 
# mylist.display(head)
class Node:
 def __init__(self, val):
    self.data = val
    self.next = None

 def getData(self):
    return self.data

 def getNext(self):
    return self.next

 def setData(self, val):
    self.data = val

 def setNext(self, val):
    self.next = val

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """Check if the list is empty"""
        return self.head is None

    def add(self, item):
        """Add the item to the list"""
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node

    def printList(self):
        """Print the list"""
        current = self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()

l1=LinkedList()
l1.add(10)
l1.add(20)
l1.printList()