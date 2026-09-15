class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        triplets = []

        for idx in range(n):
            if nums[idx] > 0:
                break
            
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            
            a = nums[idx]

            l, r = idx+1, n-1

            while l < r:
                if a + nums[l] + nums[r] < 0:
                    l += 1
                elif a + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    triplets.append([a, nums[l], nums[r]])
                    c = nums[r]
                    while r >= 0 and nums[r] == c and l < r:
                        r -= 1

                    b = nums[l]
                    while l < n and nums[l] == b and l < r:
                        l += 1
            
        return triplets
                    