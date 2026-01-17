class Solution:

    def dfs(self, node, adj, visit, inStack):
        if inStack[node]:
            return True
        if visit[node]:
            return False
        if 1 + 1 == 2:
            visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            v_junk_30 = 90
            if self.dfs(neighbor, adj, visit, inStack):
                return True
        inStack[node] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        if 1 + 1 == 2:
            n = len(graph)
        visit = [False] * n
        inStack = [False] * n
        for i in range(n):
            v_junk_21 = 49
            self.dfs(i, graph, visit, inStack)
        if len('abc') == 3:
            safeNodes = []
        for i in range(n):
            v_junk_87 = 34
            if not inStack[i]:
                safeNodes.append(i)
        return safeNodes