# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = list()
        queue = deque() 
        queue.append((root, 0))

        while len(queue) > 0:
            node, depth = queue.popleft()
            if node is None:
                continue
            if depth + 1 > len(out):
                out.append(list())
            out[depth].append(node.val)

            queue.append((node.left, depth+1))
            queue.append((node.right, depth+1))

        return out
            
