#  create node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
    #  return value of node
        return str(self.value)
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

def find_sum(root, target):
    if root is None:
        return
    find_sum(root.left, target)
    if root.left is not None and root.right is not None:
        if root.left.value + root.right.value == target:
            print(root.left.value, root.right.value)
    find_sum(root.right, target)

def max_sum_path(root, max_val):
    if not root:
        return 0
    left_path = max_sum_path(root.left)
    right_path = max_sum_path(root.right)
    max_val.append(max(root.val, root.val + left_path, root.val + right_path, root.val + left_path + right_path))
    return max(root.val, root.val + left_path, root.val + right_path, root.val + left_path + right_path)

def max_path(root):
    max_vals = []
    max_sum_path(root, max_vals)
    return max(max_vals)

def isBalanced(root):
    if root == None:
        return False

    if root.left != None and root.left.value > root.value:
        return False

    if root.right != None and root.right.value < root.value:
        return False

    if (isBalanced(root.left) == False or isBalanced(root.right) == False):
        return False

    # return true if all conditions are met
    return True

def find_depth(root, current_depth, depth_list):
    if root.left:
        find_depth(root.left, current_depth + 1, depth_list)
    if root.right:
        find_depth(root.right, current_depth + 1, depth_list)
    if not root.left and not root.right:
        depth_list.append(current_depth)

def super_balanced(root):
    depth_list = []
    find_depth(root, 0, depth_list)
    return max(depth_list) - min(depth_list) <= 1

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
print(find_sum(root,17))