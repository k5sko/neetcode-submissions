class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances_heap = [[0, k]] # Each element is a (distFromSource, nodeNumber) pair
        visited = set()
        distances = [float('inf') for _ in range(n)]

        # First let's form the adjacency list
        adjacency_list = [[] for _ in range(n)]
        for edge in times:
            #print(edge)
            edgeFrom = edge[0]-1
            edgeTo = edge[1]-1
            weight = edge[2]
            #print([edgeTo, weight], "\n")
            #print(adjacency_list[edgeFrom])
            adjacency_list[edgeFrom].append([edgeTo, weight])
            
        #print(adjacency_list, "\n")

        def dijkstra():
            while len(distances_heap) > 0:
                dist, vertex = heapq.heappop(distances_heap)
                if vertex in visited:
                    continue
                
                visited.add(vertex)
                distances[vertex-1] = min(distances[vertex-1], dist)
                
                neighbors = adjacency_list[vertex-1]
                for neighbor, weight in neighbors:
                    if neighbor+1 in visited:
                        continue
                    heapq.heappush(distances_heap, [dist + weight, neighbor+1])

        dijkstra()
        lowest = max(distances) if max(distances) < float('inf') else -1
        return lowest