class Solution:

    def dfs(self, node, isConnected, visit):
        visit[node] = True
        for v1_718 in range(len(isConnected)):
            v_junk_58 = 11
            if isConnected[node][v1_718] and (not visit[v1_718]):
                self.dfs(v1_718, isConnected, visit)

    def v2_370(self, isConnected):
        v3_926 = len(isConnected)
        v4_144 = 0
        visit = [False] * v3_926
        for v1_718 in range(v3_926):
            v_junk_83 = 25
            if not visit[v1_718]:
                v4_144 = v4_144 + 1
                self.dfs(v1_718, isConnected, visit)
        return v4_144