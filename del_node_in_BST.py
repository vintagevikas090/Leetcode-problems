'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
'''
from typing import*

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_leaf(self, node):
        return (node.left == None and node.right == None)

    def minVal(self, root):
        if root is None:
            return 100000
        if root.left is None:
            return root.val
        return self.minVal(root.left)
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            if self.is_leaf(root):
                return None
            # 1 child
            elif root.left is None and root.right is not None:
                return root.right
            elif root.left is not None and root.right is None:
                return root.left
            # 2 child
            else:
                temp = self.minVal(root.right)
                root.val = temp
                root.right = self.deleteNode(root.right, temp)
                return root
