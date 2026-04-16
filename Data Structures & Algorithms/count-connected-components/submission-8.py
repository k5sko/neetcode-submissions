class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Using a unionfind will make this really easy. We can simply connect two nodes corresponding to each edge, and then count the number of rooted trees.
        We need to implement parent-finding; path compression should make this easier.
        """
        vertices = UnionFind(n)
        for src, dest in edges:
            vertices.connect(src, dest)

        return vertices.num_parents()

class UnionFind:
    def __init__(self, num_vertices: int):
        self.vertices = [-1 for _ in range(num_vertices)]

    def __parent__(self, node: int) -> int:
        if self.vertices[node] == -1:
            return node
        else:
            return self.vertices[node]


    def connect(self, node1: int, node2: int) -> None: # O(n)
        if self.__parent__(node1) == self.__parent__(node2):
            return
        node2_parent = self.__parent__(node2)
        for vertex in range(len(self.vertices)):
            if self.__parent__(vertex) == node2_parent: # for each vertex that is in the same tree as node2
                self.vertices[vertex] = self.__parent__(node1) # we connect it directly to node1


    def num_parents(self) -> int:
        count = 0
        for num in self.vertices:
            count += num == -1
        return count