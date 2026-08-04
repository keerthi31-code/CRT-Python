class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def preorder(root):
    if root:
        preorder(root.left)
        print(root.data)
        preorder(root.right)
        

def postorder(root):
    if root:
        postorder(root.left)
        print(root.data)
        postorder(root.right)
#searching
def search(root,key):
    if root is None:
        return False
    if root.data==key:
        return True
    elif key<root.data:
        return search(root.left,key)
    else:
        return search(root.right,key)
#insertion
    def insert():

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
print("Postorder Traversal:")
postorder(root)
print("preorder:")
preorder(root)
key=80
print(search(root,key))



