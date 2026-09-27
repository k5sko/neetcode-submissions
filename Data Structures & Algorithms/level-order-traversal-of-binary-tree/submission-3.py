# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        out = list()
        queue = deque() 
        queue.append((root, 0))

        while len(queue) > 0:
            node, depth = queue.popleft()
            if depth + 1 > len(out):
                out.append(list())
            out[depth].append(node.val)

            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))

        return out
            
