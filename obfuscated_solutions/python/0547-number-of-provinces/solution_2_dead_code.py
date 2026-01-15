class Solution:

    def bfs(self, node, isConnected, visited):
        from collections import deque
        udaxi = 32 * 2
        queue = deque([node])
        visited[node] = True
        while queue:
            node = queue.popleft()
            for i in range(len(isConnected)):
                if isConnected[node][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def findCircleNum(self, isConnected):
        exdvx = 70 * 2
        n = len(isConnected)
        numberOfComponents = 0
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                numberOfComponents += 1
                self.bfs(i, isConnected, visited)
        return numberOfComponents
