class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Try to check if an edge connects two already connected nodes
        # disjoints sets will be useful here
        n = len(edges) # We know # of edges = number of vertices in this graph
        dj_set = UnionFind(n)

        for edge in edges:
            node1 = edge[0] - 1
            node2 = edge[1] - 1
            if not dj_set.connect(node1, node2):
                return edge
            
class UnionFind:
    def __init__(self, n):
        self.vertices = [-1 for _ in range(n)]

    def find_parent(self, vertex: int) -> int:
        if self.vertices[vertex] < 0:
            return vertex
        
        self.vertices[vertex] = self.find_parent(self.vertices[vertex])
        return self.vertices[vertex]

    def connect(self, node1: int, node2: int) -> bool: # returns True if they were disconnected before, False if they were connected
        parent1 = self.find_parent(node1)
        parent2 = self.find_parent(node2)
        
        if parent1 == parent2:
            return False

        # they were disconnected before; add the min weight one to the max weight one
        if self.vertices[parent1] >= self.vertices[parent2]: # if parent1 has a heavier tree
            self.vertices[parent1] += self.vertices[parent2]
            self.vertices[parent2] = parent1
        else:
            self.vertices[parent2] += self.vertices[parent1]
            self.vertices[parent1] = parent2

        return True
