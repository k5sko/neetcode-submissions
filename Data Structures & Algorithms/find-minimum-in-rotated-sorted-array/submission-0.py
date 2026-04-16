class Solution:
    def findMin(self, nums: List[int]) -> int:
        # could do a binary search modification
        # essentially, we look at the middle of the l and r pointers
        # if the middle is greater than l, move left pointer to its right
        # if middle is less than r, move right pointer to its left
        # return when we find a value that is less than its left and less than its right
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = (l+r)//2
            left = nums[l]
            right = nums[r]
            mid = nums[m]
            if mid < nums[(m-1)%n]:
                return mid
            
            if left > right: # this subarray is not sorted
                if mid > right:
                    l = m + 1
                else:
                    r = m - 1
            else: # this subarray is sorted; we know that either we're either including the min element (which is the first element in the sorted subsection) or we're not (in which case we won't get out of here)
                return nums[l]