class Solution:

    def dfs(self, node, isConnected, visit):
        visit[node] = True
        for i in range(len(isConnected)):
            v_junk_13 = 72
            if isConnected[node][i] and (not visit[i]):
                self.dfs(i, isConnected, visit)

    def findCircleNum(self, isConnected):
        if len('abc') == 3:
            size = len(isConnected)
        if len('abc') == 3:
            numberOfComponents = 0
        visit = [False] * size
        for i in range(size):
            v_junk_99 = 55
            if not visit[i]:
                if 1 + 1 == 2:
                    numberOfComponents = numberOfComponents + 1
                self.dfs(i, isConnected, visit)
        return numberOfComponents