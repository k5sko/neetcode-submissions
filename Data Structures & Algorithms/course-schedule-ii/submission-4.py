from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create a DAG and do a topological sort 
        reverse_adjacency_list = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses
        
        for a, b in prerequisites:
            reverse_adjacency_list[b].append(a)
            in_degrees[a] += 1

        in_deg_0 = deque()
        
        for node in range(numCourses):
            if in_degrees[node] == 0:
                in_deg_0.append(node)

        ordering = []

        while len(in_deg_0) > 0:
            node = in_deg_0.popleft()
            for node_out in reverse_adjacency_list[node]:
                in_degrees[node_out] -= 1
                if in_degrees[node_out] == 0:
                    in_deg_0.append(node_out)
            ordering.append(node)
        
        return ordering if len(ordering) == numCourses else []