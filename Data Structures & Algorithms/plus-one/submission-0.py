class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1

        carryOver = True

        while carryOver and i >= 0:

            if digits[i] < 9:
                carryOver = False
            
            digits[i] = (digits[i] + 1)%10
            i -= 1

        if carryOver:
            digits.insert(0, 1)

        return digits