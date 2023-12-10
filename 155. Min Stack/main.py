class MinStack:

    def __init__(self):
        self.top = -1
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.top += 1
        print(self.top)
        print(self.stack[0])
        self.stack[self.top] = val

        val = min(val, self.stack[-1] if self.minstack else val)
        self.minstack[self.top] = val

    def pop(self) -> None:
        self.stack[self.top] = 0
        self.minstack[self.top] = 0
        self.top -= 1

    def top(self) -> int:
        return self.stack[self.top]

    def getMin(self) -> int:
        return self.minstack[self.top]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()