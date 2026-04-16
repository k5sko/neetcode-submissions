class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = list()
        curr_partition = list()
        # maybe some sort of 2 pointer backtracking?
        def backtrack(idx: int) -> None: #idx can represents the index in the string up to which we've worked so far
            nonlocal partitions
            print(curr_partition, idx)
            if idx == len(s):
                if curr_partition[-1] == curr_partition[-1][::-1]:
                    partitions.append(curr_partition.copy())
                return
            
            print(s[idx])

            if len(curr_partition) == 0 or curr_partition[-1][::-1] == curr_partition[-1]:
                curr_partition.append(s[idx])
                backtrack(idx+1)
                curr_partition.pop()

            if len(curr_partition) == 0:
                return
            
            curr_partition[-1] += s[idx]
            backtrack(idx+1)
            curr_partition[-1] = curr_partition[-1][:-1]
            
        
        backtrack(0)
        return partitions
        