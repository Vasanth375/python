class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution: 

    def InsertAtFirst(self, head, data):
        '''Inserting the data at front'''
        temp = Node(data)   # creating the node
        temp.next = head    # appending the data linking the temp node main head
        head = temp         # pointing the head node to created temp node
        return head         # returing the head node


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
mylist.display(head)    ## displaying the data before adding the data at front
head = mylist.InsertAtFirst(head, 10)
mylist.display(head)


# # l=[1,2,3]
# # # print(l.__len__())
# # # print(dir(l))

# # di = {'a':1, 'b':2}
# # # print(dir(di))

# def shift_list(array, s):
#     """Shifts the elements of a list to the left or right.
#     Args:
#     array - the list to shift
#     s - the amount to shift the list ('+': right-shift, '-': left-shift)
#     Returns:
#     shifted_array - the shifted list
#     GoalKicker.com – Python® Notes for Professionals 145
#     """
#     # calculate actual shift amount (e.g., 11 --> 1 if length of the array is 5)
#     s %= len(array)
#     # reverse the shift direction to be more intuitive
#     s *= -1
#     # shift array with list slicing
#     shifted_array = array[s:] + array[:s]
#     return shifted_array
    
# my_array = [1, 2, 3, 4, 5]
#     # negative numbers
# print(shift_list(my_array, -7))