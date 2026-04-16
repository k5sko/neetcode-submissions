# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        tmp = root.right

        if root.left:
            root.right = self.invertTree(root.left)
        else:
            root.right = None

        if tmp:
            root.left = self.invertTree(tmp)
        else:
            root.left = None

        return root

"""
    1
N        2

tmp = 2

root.left = self.invertTree(2)

    2
_       _

tmp = None
root.left = None
return 2


"""