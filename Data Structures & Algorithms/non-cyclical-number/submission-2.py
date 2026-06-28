class Solution:
    def isHappy(self, n: int) -> bool:
        values = set()

        while n != 1 and n not in values:
            tmp = n
            out = 0

            while tmp != 0:
                out += (tmp%10)**2
                tmp = tmp//10

            values.add(n)
            n = out

        return (n == 1)