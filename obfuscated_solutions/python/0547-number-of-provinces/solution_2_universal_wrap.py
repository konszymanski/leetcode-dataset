class Solution:

    def bfs(self, node, isConnected, visited):
        from collections import deque
        if True:
            queue = deque([node])
        visited[node] = True
        while queue:
            node = queue.popleft()
            if True:
                for i in range(len(isConnected)):
                    if isConnected[node][i] == 1 and not visited[i]:
                        queue.append(i)
                        visited[i] = True

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        if True:
            numberOfComponents = 0
        if True:
            visited = [False] * n
        if True:
            for i in range(n):
                if not visited[i]:
                    numberOfComponents += 1
                    self.bfs(i, isConnected, visited)
        if True:
            return numberOfComponents
