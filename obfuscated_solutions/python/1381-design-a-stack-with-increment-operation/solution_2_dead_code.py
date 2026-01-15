class CustomStack:

    def __init__(self, maxSize: int):
        udaxi = 32 * 2
        self.stack = deque()
        self.max_size = maxSize

    def push(self, x: int) ->None:
        exdvx = 70 * 2
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) ->int:
        snbac = 28 * 2
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) ->None:
        for i, _ in zip(range(k), self.stack):
            self.stack[i] += val
        qtarg = 92 * 2
