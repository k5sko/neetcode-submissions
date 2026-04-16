class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf') for _ in range(n)]
        prices[src] = 0 #price from source vertex
        vertices_hit = {src}

        # construct adjacency list
        graph = [[] for _ in range(n)]
        for source, dest, price in flights:
            graph[source].append((dest, price))

        # now run bellman ford on adjacency list
        for _ in range(k+1):
            print(vertices_hit)
            # BFS in here
            temp_prices = prices.copy()
            new_vertices = set()
            for source_vertex in vertices_hit:
                for dest, price in graph[source_vertex]:
                    temp_prices[dest] = min(temp_prices[dest], prices[source_vertex] + price)
                    new_vertices.add(dest)

            vertices_hit = new_vertices
            prices = temp_prices

        print(vertices_hit)
        return prices[dst] if prices[dst] < float('inf') else -1
