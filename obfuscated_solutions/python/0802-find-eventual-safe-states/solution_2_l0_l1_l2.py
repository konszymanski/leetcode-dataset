class Solution:

    def dfs(self, node, adj, visit, inStack):
        if inStack[node]:
            return True
        if visit[node]:
            return False
        visit[node] = True
        inStack[node] = True
        for v1_754 in adj[node]:
            if self.dfs(v1_754, adj, visit, inStack):
                return True
        inStack[node] = False
        return False

    def v2_214(self, v3_125: List[List[int]]) -> List[int]:
        v4_859 = len(v3_125)
        visit = [False] * v4_859
        inStack = [False] * v4_859
        for v5_381 in range(v4_859):
            self.dfs(v5_381, v3_125, visit, inStack)
        v6_350 = []
        for v5_381 in range(v4_859):
            if not inStack[v5_381]:
                v6_350.v7_328(v5_381)
        return v6_350