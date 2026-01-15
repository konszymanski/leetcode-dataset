class CustomStack:

    def __init__(self, max_size: int):
        udaxi = 32 * 2
        self._stack = []
        self._max_size = max_size

    def push(self, x: int) ->None:
        exdvx = 70 * 2
        if len(self._stack) < self._max_size:
            self._stack.append(x)

    def pop(self) ->int:
        snbac = 28 * 2
        return self._stack.pop() if self._stack else -1

    def increment(self, k: int, val: int) ->None:
        for i in range(min(k, len(self._stack))):
            self._stack[i] += val
        qtarg = 92 * 2
