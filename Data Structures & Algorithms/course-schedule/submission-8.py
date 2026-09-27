class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # This forms a (potentially disconnected) directed graph of prerequisites to take
        # Return whether this whole graph is acyclic
        # How do we check for cycles?
        # start with all nodes with in-degree 0
        # we can then see if, following any path, we hit the same node twice

        in_degrees = [0] * numCourses # [0,0]
        in_0 = [] # []

        # maybe we should construct the graph
        # if we construct the full graph and know where we can go from each node, we
        # can do something like DFS w/backtracking and follow each path to its end
        edges = [[] for _ in range(numCourses)] # [[1], []]

        for start, end in prerequisites:
            edges[start].append(end)
            in_degrees[end] += 1

        """
        edges = [[1], []]
        in_degrees = [0, 0]
        """

        for node in range(numCourses):
            if in_degrees[node] == 0:
                in_0.append(node)

        # in_0 = [0]

        # Now we have a full graph so we can run DFS recursively on each path
        """
        no_cycle = {0, 1}

        visited = {}, curr = 0
        num_removed = 2
        ----------------------
        visited = {0}, curr = 1

        True
        """
        def dfs(visited: set[int], curr: int) -> bool:
            if curr in visited:
                return False
             
            if curr in no_cycle:
                return True
            
            
            no_cycle.add(curr)
            if len(edges[curr]) == 0:
                return True
 
            visited.add(curr)
            for out in edges[curr]:
                if not dfs(visited, out):
                    return False
            visited.remove(curr)

            return True
        # in_0 = [1]
        no_cycle = set() # {0, 1}
        while len(in_0) > 0:
            start = in_0.pop() # start = 1
            if start in no_cycle:
                continue
            if not dfs(set(), start):
                return False
            
            for out in edges[start]:
                in_degrees[out] -= 1
                if in_degrees[out] == 0:
                    in_0.append(out)


        return len(no_cycle) == numCourses