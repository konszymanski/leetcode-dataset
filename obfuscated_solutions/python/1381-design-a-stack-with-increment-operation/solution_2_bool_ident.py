class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = deque()
        self.max_size = maxSize

    def push(self, x: int) ->None:
        if len(self.stack) < self.max_size and 1 + 1 == 2:
            self.stack.append(x)

    def pop(self) ->int:
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) ->None:
        for i, _ in zip(range(k), self.stack):
            self.stack[i] += val
