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
        print(root.data)
        preorder(root.left)
        preorder(root.right)
        

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
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
def insert(root,key):
    if root is None:
        return Node(key)
    if key<root.data:
        root.left=insert(root.left,key)
    elif key>root.data:
        root.right=insert(root.right,key)
    return root
def deletion(root,key):
    if root is None:
        return None
    if key<root.data:
        root.left=deletion(root.left,key)
    elif key>root.data:
        root.right=deletion(root.right,key)
    else:
        if root.left is None and root.right is None:
            return None
    return root
def delete_one(root,key):
    if root is None:
        return None
    if key<root.data:
        root.left=delete_one(root.left, key)
    elif key>root.data:
        root.right=delete_one(root.right,key)
    else:
        if root.right is None:
            return root.left
        else:
            return root.right
    return root
def delete_root(root,key):
# we can delete root either from replacing mimimum element of right subtree or max eleminent fron left subtree
    if root is None:
            return None
    if key<root.data:
            root.left=delete_root(root.left, key)
    elif key>root.data:
            root.right=delete_root(root.right,key)
    else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp=root.right
            while temp.left:
                temp=temp.left
            root.data=temp.data
            root.right=delete_root(root.right,temp.data)
    return root

root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)

print("Inorder:")
inorder(root)

print("Search:", search(root, 15))

root = insert(root, 25)

print("After Insert:")
inorder(root)

root = deletion(root, 10)

print("After Delete:")
inorder(root)

root=delete_one(root, 15)
print("after deletion one node:")
inorder(root)
root=delete_root(root, 20)
print("after deletion of root:")
inorder(root)

