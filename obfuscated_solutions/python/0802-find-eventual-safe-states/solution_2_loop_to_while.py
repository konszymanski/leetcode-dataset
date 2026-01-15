class Solution:

    def dfs(self, node, adj, visit, inStack):
        if inStack[node]:
            return True
        if visit[node]:
            return False
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True
        inStack[node] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) ->List[int]:
        n = len(graph)
        visit = [False] * n
        inStack = [False] * n
        i = 0
        while i < n:
            self.dfs(i, graph, visit, inStack)
            i += 1
        safeNodes = []
        i = 0
        while i < n:
            if not inStack[i]:
                safeNodes.append(i)
            i += 1
        return safeNodes
