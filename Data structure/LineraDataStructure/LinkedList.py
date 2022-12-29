'''
Linked List TODO: 
Basic Insertion(appending at back defaultly)
Insert at Front
Insert at Back
Insert at middle
Delete at Front
Delete at middle
Delete at Back
Search for an data
Delete only specific data
sort the Nodes
Remove Duplicates
'''


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution: 

    def search(self, data):
        '''searches for an element and returns a string with found data'''
        if head:
            curr = head
            while curr:
                if curr.data == data:
                    return "Match Found! "+ str(curr.data)
                curr = curr.next
        return "Match not Found:("

    def getLength(self, head):
        '''returns the length of the linkedlist'''
        curr = head
        length = 0
        while curr:
            length+=1
            curr = curr.next
        return length

    def deleteRear(self, head):
        '''this will deletes the last element from the linkedlist and returns the list'''
        curr = head
        if curr:
            for i in range(1,self.getLength(head)-1):
                curr = curr.next
            curr.next = None
        else:
            print("LinkedList is empty")
        return head

    def deleteFront(self, head):
        '''Return the head after deleting 
            the first node. In case Node is None It prints a string and returns head'''
        temp = head
        if head == None:
            print("Linked List is Empty, Suggested to the Insert data")
            return head

        head = head.next
        temp.next = None
        return head
        
    def InsertAtFirst(self, head, data):
        '''Inserting the data at front'''
        temp = Node(data)   # creating the node
        temp.next = head    # appending the data linking the temp node main head
        head = temp         # pointing the head node to created temp node
        return head         # returing the head node

    def InsertAtEnd(self, head, data):
        '''Inserting element at back'''
        temp = Node(data)
        currentNode = head
        while currentNode:
            if currentNode.next == None:
                currentNode.next = temp
                break
            currentNode = currentNode.next 

    def display(self,head):
        '''display method will traverse through linked list and display each data in it'''

        current = head  # current points to head
                
        while current:  # checking if current is pointing to None or not
            print(current.data,end=' ')
            current = current.next  # current is now pointing to next node
        print()

    def insert(self,head,data): 
        '''Insert method used to creating new data 
            to existing data or very basic level of
             linkedlist insertion'''
            
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

    def sortList(self, head):  
        #Node current will point to head  
        current = head;  
        index = None;  
          
        if(head == None):  
            return;  
        else:  
            while(current != None):  
                #Node index will point to node next to current  
                index = current.next;  
                  
                while(index != None):  
                    #If current node's data is greater than index's node data, swap the data between them  
                    if(current.data > index.data):  
                        temp = current.data;  
                        current.data = index.data;  
                        index.data = temp;  
                    index = index.next;  
                current = current.next;  


mylist= Solution()
# T=int(input("Enter the nodes you want to Insert: "))
a = [3,1,2, 8,0, 7, 6, 3, 4, 9, 5]
T = len(a)
head=None
data=0
for i in range(T):
    data=a[i]
    head=mylist.insert(head,data)  

mylist.display(head)    ## displaying the data before adding the data at front
mylist.sortList(head)        

# head = mylist.InsertAtFirst(head, 0)
# head = mylist.InsertAtFirst(head, -1)

# mylist.InsertAtEnd(head, 4)
# mylist.InsertAtEnd(head, 5)

# head = mylist.deleteFront(head)
# head = mylist.deleteFront(head)

mylist.display(head)

# print(mylist.getLength(head))
# head = mylist.deleteRear(head)
# mylist.display(head)

#print(mylist.search(3))




# # l=[1,2,3]
# # # print(l.__len__())
# # # print(dir(l))

# # di = {'a':1, 'b':2}
# # # print(dir(di))