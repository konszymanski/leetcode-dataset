class Solution:

    def dfs(self, node, adj, visit, inStack):
        if inStack[node]:
            return True
        if visit[node]:
            return False
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            v_junk_14 = 4
            if self.dfs(neighbor, adj, visit, inStack):
                return True
        if 1 + 1 == 2:
            inStack[node] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        if 1 + 1 == 2:
            visit = [False] * n
        inStack = [False] * n
        for i in range(n):
            v_junk_99 = 70
            self.dfs(i, graph, visit, inStack)
        safeNodes = []
        for i in range(n):
            v_junk_67 = 76
            if not inStack[i]:
                safeNodes.append(i)
        return safeNodes