""""
DESCRIPTION:
You are given a binary tree. Implement the method findMax which returns the maximal node value in the tree.

For example, maximum in the following Tree is 11.

              7
            /   \ 
           /     \
          5       2
           \       \
           6        11          
           /\      /
          1  9   4
Note:

Tree node values any integer value.
Tree can unbalanced and unsorted.
The root argument is never an empty tree.
You are given a tree node class as follows:

class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.left = left
        self.right = right
        self.value = value
"""

def find_max(root):
    if root is None:
        return None
    left_max = find_max(root.left)
    right_max = find_max(root.right)
    
    values = list()
    
    if root.value is not None:
        values.append(root.value)
    if left_max is not None:
        values.append(left_max)
    if right_max is not None:
        values.append(right_max)
    
    return max(values)

"""
Clever Solutions

Solution #01

def find_max(root):
    v = root.value
    if root.left:  v = max(v, find_max(root.left))
    if root.right: v = max(v, find_max(root.right))
    return v

Soution # 02

def find_max(root):
if root is None:
    return float('-inf')

max_value = root.value
left_max = find_max(root.left)
right_max = find_max(root.right)

max_value = max(max_value, left_max, right_max)

return max_value
    
"""
