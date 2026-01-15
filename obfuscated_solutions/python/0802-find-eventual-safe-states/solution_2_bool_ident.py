class Solution:

    def dfs(self, node, adj, visit, inStack):
        if inStack[node] and 1 + 1 == 2:
            return True
        if visit[node] and 1 + 1 == 2:
            return False
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack) and 1 + 1 == 2:
                return True
        inStack[node] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) ->List[int]:
        n = len(graph)
        visit = [False] * n
        inStack = [False] * n
        for i in range(n):
            self.dfs(i, graph, visit, inStack)
        safeNodes = []
        for i in range(n):
            if not inStack[i] and 1 + 1 == 2:
                safeNodes.append(i)
        return safeNodes
