'''
Operations of BST:
Insertion
Searching
Deletion

Auxiliary operations
Find the height of tree
Find number of levels in BST
Find the maximum value in the BST
'''

class Node(object):
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.val = val

        
class BinarySearchTree(object):

    """Basic Operations"""
    def insert(self, root, node):
        if root is None:
            return node
        if root.val < node.val:
            root.r_child = self.insert(root.r_child, node)
        else:
            root.l_child = self.insert(root.l_child, node)
        return root

    def search(self, root, key):
        if root is None:
            return "Data Not Found or Tree is empty"
        if root.val == key:
            return "Found it"
        elif root.val < key:
            return self.search(root.r_child, key)
        elif root.val > key:
            return self.search(root.l_child, key)
    
    """BST Traversals"""
    def in_order_place(self, root):
        if not root:
            return None
        else:
            self.in_order_place(root.l_child)
            print( root.val)
            self.in_order_place(root.r_child)

    def pre_order_place(self, root):
        if not root:
            return None
        else:
            print( root.val)
            self.pre_order_place(root.l_child)
            self.pre_order_place(root.r_child)

    def post_order_place(self, root):
        if not root:
            return None
        else:
            self.post_order_place(root.l_child)
            self.post_order_place(root.r_child)
            print( root.val)

""" Create different node and insert data into it"""
r = Node(3)     # creating root node with choosing 3 as root node value
node = BinarySearchTree()

nodeList = [1, 8, 5, 12, 14, 6, 15, 7, 16, 8]
for nd in nodeList:
    node.insert(r, Node(nd))

print(node.search(r, 12))

# print( "------In order ---------")
# print(node.in_order_place(r))

# print( "------Pre order ---------")
# print(node.pre_order_place(r))

# print( "------Post order ---------")
# print(node.post_order_place(r))