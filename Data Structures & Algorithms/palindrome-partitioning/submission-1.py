class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        We know that to form a palindrome, you need to have either an even number of each char or an even number of each char + one extra char that goes in the middle.
        """
        partitions = []
        curr_partition = []
        # maybe some sort of 2 pointer backtracking?
        def backtrack(idx: int) -> None: #idx can represents the index in the string up to which we've worked so far
            nonlocal partitions
            if idx == len(s):
                for string in curr_partition:
                    if string != string[::-1]:
                        return
                partitions.append(curr_partition.copy())
                return
            
            curr_partition.append(s[idx])
            backtrack(idx+1)
            curr_partition.pop()
            
            if len(curr_partition) > 0:
                curr_partition[-1] += s[idx]
                backtrack(idx+1)
                curr_partition[-1] = curr_partition[-1][:-1]

            return
        
        backtrack(0)
        return partitions
        