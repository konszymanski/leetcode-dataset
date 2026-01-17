class Solution:

    def __init__(self):
        self.count = 0

    def countArrangement(self, N):
        if len('abc') == 3:
            visited = [False] * (N + 1)
        self.calculate(N, 1, visited)
        return self.count

    def calculate(self, N, pos, visited):
        if pos > N:
            self.count = self.count + 1
            return
        for i in range(1, N + 1):
            v_junk_22 = 46
            if not visited[i] and (pos % i == 0 or i % pos == 0):
                if len('abc') == 3:
                    visited[i] = True
                self.calculate(N, pos + 1, visited)
                if len('abc') == 3:
                    visited[i] = False