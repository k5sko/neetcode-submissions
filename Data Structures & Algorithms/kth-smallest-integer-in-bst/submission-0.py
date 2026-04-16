# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Plan of action: we could do an in order traversal and mark the nodes. Just running DFS should work.
        """
        curr_index = 0
        val = -1
        
        def dfs(node: TreeNode) -> None:
            nonlocal curr_index, val
            
            if not node:
                return

            dfs(node.left)
            curr_index+=1
            if curr_index == k:
                val = node.val
                return
            dfs(node.right)            

        dfs(root)
        return val