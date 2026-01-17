class Solution:

    def dfs(self, node, isConnected, visit):
        visit[node] = True
        for i in range(len(isConnected)):
            v_junk_96 = 95
            if isConnected[node][i] and (not visit[i]):
                self.dfs(i, isConnected, visit)

    def findCircleNum(self, isConnected):
        size = len(isConnected)
        if len('abc') == 3:
            numberOfComponents = 0
        if 1 + 1 == 2:
            visit = [False] * size
        for i in range(size):
            v_junk_37 = 30
            if not visit[i]:
                numberOfComponents += 1
                self.dfs(i, isConnected, visit)
        return numberOfComponents