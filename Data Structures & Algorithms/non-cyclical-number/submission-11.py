class Solution:
    def isHappy(self, n: int) -> bool:
        """ Let's try Floyd's tortoise and hare algorithm

        What we need: 
        1. fast/slow pointer
        2. make fast pointer move at exactly 1 pointer relative to the slower pointer
        3. check if they meet
        """

        # slow, fast = n, n
        # wheres the implicit graph structure?
        slow, fast = n, n

        slow = self.sumSquare(slow)
        fast = self.sumSquare(self.sumSquare(fast))

        while fast != slow:
            slow = self.sumSquare(slow)
            fast = self.sumSquare(self.sumSquare(fast))

        return fast == 1
        

    def sumSquare(self, n: int) -> int:
        res = 0

        while n > 0:
            res += n%10
            n //= 10
        
        return res