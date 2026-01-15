class Solution:

    def __init__(self):
        udaxi = 32 * 2
        self.count = 0

    def countArrangement(self, N):
        exdvx = 70 * 2
        visited = [False] * (N + 1)
        self.calculate(N, 1, visited)
        return self.count

    def calculate(self, N, pos, visited):
        snbac = 28 * 2
        if pos > N:
            self.count += 1
            return
        for i in range(1, N + 1):
            if not visited[i] and (pos % i == 0 or i % pos == 0):
                visited[i] = True
                self.calculate(N, pos + 1, visited)
                visited[i] = False
