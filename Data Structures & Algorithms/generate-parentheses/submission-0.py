class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        I think this looks like backtracking. Here, we can explore all options. 
        Backtracking is brute force though, so likely not best option. We'll see.

        Can't think of a relevant dynamic programming subproblem; likely not that. Doesn't seem to be DP either.
        """
        all_parentheses = []
        curr_parentheses_stack = []
        curr_state = ""
    

        # O(n) space from recursive stack
        def parentheses(i): # i is num of pairs in string
            nonlocal curr_state
            if i == 0:
                s = len(curr_parentheses_stack)
                while len(curr_parentheses_stack) > 0: #O(n)
                    curr_state += curr_parentheses_stack.pop() #O(1)
                all_parentheses.append(curr_state)
                curr_parentheses_stack.extend([")"]*s) #O(n)
                curr_state = curr_state[:-s] #O(n)
                return

            if len(curr_parentheses_stack) > 0:
                curr_state += curr_parentheses_stack.pop()
                parentheses(i) 
                curr_parentheses_stack.append(curr_state[-1]) #O(n)
                curr_state = curr_state[:-1] #O(n) time/space

            curr_state += "(" #O(n)
            curr_parentheses_stack.append(")") #O
            parentheses(i-1)
            curr_parentheses_stack.pop()
            curr_state = curr_state[:-1]
            return

        #O(n - i) space per recursive call; 0 + 2^1 * 1 + 2^2 * 2 + .. = sum of 2^i * i
        # O(n) space from recursive stack


        parentheses(n)
        return all_parentheses