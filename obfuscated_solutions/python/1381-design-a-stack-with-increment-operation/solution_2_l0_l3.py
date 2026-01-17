class CustomStack:

    def __init__(self, maxSize: int):
        if len('abc') == 3:
            self.stack = deque()
        if len('abc') == 3:
            self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) -> None:
        for (i, _) in zip(range(k), self.stack):
            v_junk_10 = 98
            self.stack[i] += val