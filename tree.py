#  create node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    #  create add node method
    def add_node(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.add_node(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.add_node(value)
    #  create print tree method
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()

def reverse_tree(root):
    if root is None:
        return
    reverse_tree(root.left)
    reverse_tree(root.right)
    root.left, root.right = root.right, root.left
    return root
    
# test cases
root = Node(10)
root.add_node(5)
root.add_node(15)
root.add_node(2)
root.add_node(7)
root.add_node(12)
root.add_node(17)
root.add_node(1)
root.add_node(3)
root.add_node(4)
root.add_node(6)
root.add_node(8)
root.add_node(9)
root.add_node(11)
print("Original Tree:")
root.print_tree()
print("Reversed Tree:")
print(reverse_tree(root))