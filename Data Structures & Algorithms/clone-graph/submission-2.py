from copy import deepcopy 
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        
        nodesToVisited = dict()

        def dfs(node):            
            new_node = deepcopy(node)
            new_node.neighbors = []

            if node in nodesToVisited.keys():
                return nodesToVisited[node]

            nodesToVisited[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            
            return new_node
        
        return dfs(node)

"""
visited = {1}
"""