class Solution:

    def dfs(self, node, isConnected, visit):
        visit[node] = True
        i = 0
        while i < len(isConnected):
            if isConnected[node][i] and not visit[i]:
                self.dfs(i, isConnected, visit)
            i += 1

    def findCircleNum(self, isConnected):
        size = len(isConnected)
        numberOfComponents = 0
        visit = [False] * size
        i = 0
        while i < size:
            if not visit[i]:
                numberOfComponents += 1
                self.dfs(i, isConnected, visit)
            i += 1
        return numberOfComponents
