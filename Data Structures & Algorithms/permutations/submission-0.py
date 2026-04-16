class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        current_state = []
        def dfs():
            if len(current_state) == len(nums):
                permutations.append(current_state.copy())

            for i in nums:
                if i not in current_state:
                    current_state.append(i)
                    dfs()
                    current_state.remove(i)

        dfs()
        return permutations