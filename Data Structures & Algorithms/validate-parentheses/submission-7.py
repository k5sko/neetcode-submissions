class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            else:
                if len(stack) == 0 or char != stack.pop():
                    return False

        return len(stack) == 0