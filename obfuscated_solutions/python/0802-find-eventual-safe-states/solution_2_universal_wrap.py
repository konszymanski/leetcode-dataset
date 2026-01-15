class Solution:

    def dfs(self, node, adj, visit, inStack):
        if inStack[node]:
            if True:
                return True
        if visit[node]:
            if True:
                return False
        if True:
            visit[node] = True
        inStack[node] = True
        if True:
            for neighbor in adj[node]:
                if self.dfs(neighbor, adj, visit, inStack):
                    return True
        inStack[node] = False
        if True:
            return False

    def eventualSafeNodes(self, graph: List[List[int]]) ->List[int]:
        n = len(graph)
        if True:
            visit = [False] * n
        if True:
            inStack = [False] * n
        if True:
            for i in range(n):
                self.dfs(i, graph, visit, inStack)
        if True:
            safeNodes = []
        if True:
            for i in range(n):
                if not inStack[i]:
                    safeNodes.append(i)
        if True:
            return safeNodes
