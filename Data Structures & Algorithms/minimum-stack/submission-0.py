class MinStack:
    def __init__(self):
        self.elems = []
        self.prefixed_min_stack = [float('inf')] # treat this like a stack

    def push(self, val: int) -> None:
        self.elems.append(val)
        self.prefixed_min_stack.append(min(val, self.prefixed_min_stack[-1]))

    def pop(self) -> None:
        self.elems.pop(-1)
        self.prefixed_min_stack.pop(-1)

    def top(self) -> int:
        return self.elems[-1]

    def getMin(self) -> int:
        return self.prefixed_min_stack[-1]
        
