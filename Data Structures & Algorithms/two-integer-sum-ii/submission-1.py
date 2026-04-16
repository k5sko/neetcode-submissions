class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        forward = 1
        backward = len(numbers)
        
        while forward < backward:
            f = numbers[forward-1]
            b = numbers[backward-1]
            if f + b == target:
                return [forward, backward]
            elif f + b < target:
                forward+=1
            else:
                backward-=1