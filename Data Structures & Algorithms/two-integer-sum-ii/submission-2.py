class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while True:
            if numbers[l] + numbers[r] == target:
                return list((l+1, r+1))
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1