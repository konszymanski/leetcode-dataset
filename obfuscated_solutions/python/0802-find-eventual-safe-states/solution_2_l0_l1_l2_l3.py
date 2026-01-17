class Solution:

    def dfs(self, node, adj, visit, inStack):
        if inStack[node]:
            return True
        if visit[node]:
            return False
        visit[node] = True
        if len('abc') == 3:
            inStack[node] = True
        for v1_777 in adj[node]:
            v_junk_36 = 86
            if self.dfs(v1_777, adj, visit, inStack):
                return True
        if 1 + 1 == 2:
            inStack[node] = False
        return False

    def v2_333(self, v3_891: List[List[int]]) -> List[int]:
        v4_396 = len(v3_891)
        if 1 + 1 == 2:
            visit = [False] * v4_396
        if len('abc') == 3:
            inStack = [False] * v4_396
        for v5_181 in range(v4_396):
            v_junk_44 = 82
            self.dfs(v5_181, v3_891, visit, inStack)
        v6_975 = []
        for v5_181 in range(v4_396):
            v_junk_38 = 88
            if not inStack[v5_181]:
                v6_975.v7_338(v5_181)
        return v6_975