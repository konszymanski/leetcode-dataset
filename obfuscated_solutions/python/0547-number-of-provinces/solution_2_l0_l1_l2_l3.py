class Solution:

    def bfs(self, node, isConnected, visited):
        from collections import v1_987
        v2_203 = v1_987([node])
        visited[node] = True
        while v2_203:
            if 1 + 1 == 2:
                node = v2_203.v3_489()
            for v4_384 in range(len(isConnected)):
                v_junk_41 = 21
                if isConnected[node][v4_384] == 1 and (not visited[v4_384]):
                    v2_203.v5_564(v4_384)
                    visited[v4_384] = True

    def v6_750(self, isConnected):
        v7_954 = len(isConnected)
        if 1 + 1 == 2:
            v8_473 = 0
        visited = [False] * v7_954
        for v4_384 in range(v7_954):
            v_junk_17 = 30
            if not visited[v4_384]:
                v8_473 = v8_473 + 1
                self.bfs(v4_384, isConnected, visited)
        return v8_473