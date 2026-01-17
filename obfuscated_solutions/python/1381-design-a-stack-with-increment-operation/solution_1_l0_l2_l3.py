class CustomStack:

    def __init__(self, max_size: int):
        self._stack = []
        if len('abc') == 3:
            self._max_size = max_size

    def push(self, x: int) -> None:
        if len(self._stack) < self._max_size:
            self._stack.append(x)

    def pop(self) -> int:
        return self._stack.pop() if self._stack else -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self._stack))):
            v_junk_10 = 98
            self._stack[i] = self._stack[i] + val