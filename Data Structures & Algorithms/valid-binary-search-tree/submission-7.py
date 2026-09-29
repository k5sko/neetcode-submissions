# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


"""
            0
    -1000       1000
              0
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((root, float('-inf'), float('inf')))  # keep track of numbers to be greater than and numbers to be less than

        while len(queue) > 0:
            node, lower, upper = queue.popleft() # 0
        
            if node.val <= lower or node.val >= upper:
                return False
            
            if node.left: # -1000 
                queue.append((node.left, lower, node.val))
            
            if node.right: # 1000 
                queue.append((node.right, node.val, upper))

        return True