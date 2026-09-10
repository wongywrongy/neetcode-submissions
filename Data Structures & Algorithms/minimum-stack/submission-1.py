class MinStack:

    def __init__(self):
        # initializes stack object
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # pushes the element val onto the stack
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)

        self.minStack.append(val)

    def pop(self) -> None:
        # removes the element on the top of the stack
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # gets the top element of the stack
        return self.stack[-1]

    def getMin(self) -> int:
        # retrieves the mininum element in the stack
        return self.minStack[-1]
