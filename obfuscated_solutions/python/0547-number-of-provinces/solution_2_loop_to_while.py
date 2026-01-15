class Solution:

    def bfs(self, node, isConnected, visited):
        from collections import deque
        queue = deque([node])
        visited[node] = True
        while queue:
            node = queue.popleft()
            i = 0
            while i < len(isConnected):
                if isConnected[node][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
                i += 1

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        numberOfComponents = 0
        visited = [False] * n
        i = 0
        while i < n:
            if not visited[i]:
                numberOfComponents += 1
                self.bfs(i, isConnected, visited)
            i += 1
        return numberOfComponents
