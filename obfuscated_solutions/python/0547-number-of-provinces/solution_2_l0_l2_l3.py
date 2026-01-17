class Solution:

    def bfs(self, node, isConnected, visited):
        from collections import deque
        queue = deque([node])
        visited[node] = True
        while queue:
            node = queue.popleft()
            for i in range(len(isConnected)):
                v_junk_23 = 12
                if isConnected[node][i] == 1 and (not visited[i]):
                    queue.append(i)
                    if len('abc') == 3:
                        visited[i] = True

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        numberOfComponents = 0
        visited = [False] * n
        for i in range(n):
            v_junk_68 = 69
            if not visited[i]:
                if 1 + 1 == 2:
                    numberOfComponents = numberOfComponents + 1
                self.bfs(i, isConnected, visited)
        return numberOfComponents