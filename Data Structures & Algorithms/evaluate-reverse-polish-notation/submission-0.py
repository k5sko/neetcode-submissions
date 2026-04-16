class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        I believe that the solution to this should involve some sort of stack. Since arithmetic involves two numbers, what I can do is keep adding to the stack the result of the most recent operation until we reach the end.
        """
        stack = []
        print(abs(6 * (-132))//(6*(-132)) * abs(6)//abs(-132))
        for token in tokens:
            stack.append(token)
            if token == "+":
                stack.pop()
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(str(first + second))
            elif token == "-":
                stack.pop()
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(str(first - second))
            elif token == "*":
                stack.pop()
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(str(first * second))
            elif token == "/":
                stack.pop()
                second = int(stack.pop())
                first = int(stack.pop())
                #insert = abs(first//second)//(first//second) * abs(first)//abs(second)
                if first == 0:
                    insert = 0
                else:
                    insert = abs(first * second)//(first*second) * (abs(first)//abs(second))
                stack.append(str(insert))

        # 6/-132 = 
        return int(stack[0])