# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Something to do with BFS as that will go layer by layer.
        # Or, maybe try something recursive
        # Maybe I could create a data structure to tell us the depth of each subtree? but how would you index into it; what identifies a subtree? values don't seem to be unique
        # Maybe values are unique, let's try
    
        depthOfTree = defaultdict()

        def depthIsEqual(parent: Optional[TreeNode]) -> int: 
            if not parent:
                return True

            if not parent.left and not parent.right:
                depthOfTree[parent] = 1
                return True
            elif not parent.left and parent.right:
                balanced = depthIsEqual(parent.right) 
                depthOfTree[parent] = 1 + depthOfTree[parent.right]
                return balanced and depthOfTree[parent.right] <= 1
            elif not parent.right and parent.left:
                balanced = depthIsEqual(parent.left)
                depthOfTree[parent] = 1 + depthOfTree[parent.left]
                return balanced and depthOfTree[parent.left] <= 1
            else:
                balanced = depthIsEqual(parent.left) 
                balanced = depthIsEqual(parent.right) and balanced
                depthOfTree[parent] = 1 + max(depthOfTree[parent.left], depthOfTree[parent.right])
                return balanced and abs(depthOfTree[parent.right] - depthOfTree[parent.left]) <= 1
            

        return depthIsEqual(root)