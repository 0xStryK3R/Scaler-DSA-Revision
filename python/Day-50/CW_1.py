class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.main_stack.append(x)
        if not self.min_stack or self.min_stack[-1] > x:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    # @return nothing
    def pop(self):
        x = None
        if self.main_stack:
            x = self.main_stack.pop()
            self.min_stack.pop()
        return x

    # @return an integer
    def top(self):
        x = -1
        if self.main_stack:
            x = self.main_stack[-1]
        return x

    # @return an integer
    def getMin(self):
        x = -1
        if self.min_stack:
            x = self.min_stack[-1]
        return x
