class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        in_degrees = [0] * numCourses  # [1, 0]
        edges = [[] for _ in range(numCourses)] # [[], [0]]
        num_0 = 0
        for end, start in prerequisites:
            edges[start].append(end)
            in_degrees[end] += 1

        zero_in = deque()
        for idx in range(numCourses):
            if in_degrees[idx] == 0:
                zero_in.append(idx)
        # zero_in = [1]
        # num_0 = 1
    
        while len(zero_in) > 0:
            node = zero_in.popleft() # node = 1
            num_0 += 1
            for out in edges[node]:
                in_degrees[out] -= 1
                if in_degrees[out] == 0:
                    zero_in.append(out)
        
        return num_0 == numCourses