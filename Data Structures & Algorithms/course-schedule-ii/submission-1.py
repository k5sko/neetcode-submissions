from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # so we see that there are prerequisites
        """
        Note that the prereqs can be modeled as directed edges prereq -> course
        """
        # We can see that there's some sort of implicit DAG structure in this problem
        # Maybe we can do a topological sort

        # First, create an adjacency list for the DAG; let's keep it in reverse order
        adj_list = [[] for _ in range(numCourses)]
        r_adj_list = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            r_adj_list[course].append(prereq)

        deg_to_node = [[] for _ in range(numCourses)]
        node_to_deg = [0 for _ in range(numCourses)]
        for node in range(len(adj_list)):
            node_to_deg[node] = len(r_adj_list[node]) # the in-degree of a noed is the number of edges going into it, or the number of edges going out of it in the reverse graph

        for node in range(len(node_to_deg)):
            deg_to_node[node_to_deg[node]].append(node) # we map deg(node) -> node
        # then we can topological sort the nodes using the DAG
        # for each node with in-degree 0, remove from adjacency list and add to sorted_order           
        sorted_order = list()

        def topo_sort() -> None:
            nonlocal sorted_order
            visited = set()
            while len(deg_to_node[0]) > 0:
                insert = deg_to_node[0].pop()
                neighbors = adj_list[insert]
                sorted_order.append(insert)
                visited.add(insert)

                for neighbor in neighbors:
                    if neighbor not in visited and node_to_deg[neighbor] > 0:
                        deg = node_to_deg[neighbor]
                        deg_to_node[deg].remove(neighbor)
                        deg_to_node[deg-1].append(neighbor)
                        node_to_deg[neighbor] -= 1

        # return the topological sort
        topo_sort()
        return sorted_order if len(sorted_order) == numCourses else []