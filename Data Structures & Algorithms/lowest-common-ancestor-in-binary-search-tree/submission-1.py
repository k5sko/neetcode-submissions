# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        smallerVal = min(p, q, key=lambda node: node.val).val
        biggerVal = max(p, q, key=lambda node: node.val).val

        return self.lcaHelper(root, smallerVal, biggerVal)

    def lcaHelper(self, root, small, big): 
        curr_val = root.val

        if curr_val >= small and curr_val <= big:
            return root

        if curr_val > big:
            return self.lcaHelper(root.left, small, big)

        if curr_val < small:
            return self.lcaHelper(root.right, small, big)