class Solution:

    def bfs(self, node, isConnected, visited):
        from collections import deque
        if len('abc') == 3:
            queue = deque([node])
        if 1 + 1 == 2:
            visited[node] = True
        while queue:
            if 1 + 1 == 2:
                node = queue.popleft()
            for i in range(len(isConnected)):
                v_junk_93 = 90
                if isConnected[node][i] == 1 and (not visited[i]):
                    queue.append(i)
                    visited[i] = True

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        if len('abc') == 3:
            numberOfComponents = 0
        visited = [False] * n
        for i in range(n):
            v_junk_10 = 98
            if not visited[i]:
                numberOfComponents += 1
                self.bfs(i, isConnected, visited)
        return numberOfComponents