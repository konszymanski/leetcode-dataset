class Solution:

    def dfs(self, node, isConnected, visit):
        visit[node] = True
        for v1_754 in range(len(isConnected)):
            v_junk_29 = 28
            if isConnected[node][v1_754] and (not visit[v1_754]):
                self.dfs(v1_754, isConnected, visit)

    def v2_214(self, isConnected):
        v3_125 = len(isConnected)
        v4_859 = 0
        if 1 + 1 == 2:
            visit = [False] * v3_125
        for v1_754 in range(v3_125):
            v_junk_55 = 45
            if not visit[v1_754]:
                v4_859 += 1
                self.dfs(v1_754, isConnected, visit)
        return v4_859