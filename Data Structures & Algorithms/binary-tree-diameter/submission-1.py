# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        diam = 0

        left_depth = 
        """

        diam = 0

        # dfs store left/right depth
        def max_depth(node: Optional[TreeNode]) -> int:
            nonlocal diam
            if not node: 
                return -1
            
            left_depth = max_depth(node.left) + 1
            right_depth = max_depth(node.right) + 1

            diam = max(left_depth + right_depth, diam)
            return max(left_depth, right_depth)
        
        max_depth(root)

        return diam