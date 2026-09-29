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
        queue.append(root)

        while len(queue) > 0:
            node = queue.popleft()
            if node.left:
                if node.val <= node.left.val:
                    return False
                
                queue.append(node.left)
            
            if node.right:
                if node.right.val <= node.val:
                    return False
                
                queue.append(node.right)

        return True