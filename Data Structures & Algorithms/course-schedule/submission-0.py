from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0 for _ in range(numCourses)]
        adjacency_list = [[] for _ in range(numCourses)]
        topo_sort = deque()
        in_zero = deque() # nodes with in-degree 0

        for course, prereq in prerequisites:
            in_degree[course] += 1
            adjacency_list[prereq].append(course)

        # now that we have an adjacency list and in-degree list, we can start iterating on courses that have in-degree 0 (this is kahn's algorithm)

        # lets first figure out which nodes have in-degree 0
        for course in range(numCourses):
            if in_degree[course] == 0:
                in_zero.append(course)

        # now that we have nodes with in-degree 0, let's see which nodes are adjacent to them and do an iteration
        while len(in_zero) > 0:
            node_visited = in_zero.popleft()
            topo_sort.append(node_visited)

            neighbors = adjacency_list[node_visited]
            for neighbor in neighbors:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    in_zero.append(neighbor)                

        return len(topo_sort) == numCourses