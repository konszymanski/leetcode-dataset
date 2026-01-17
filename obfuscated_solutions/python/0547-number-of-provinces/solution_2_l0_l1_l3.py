class Solution:

    def bfs(self, node, isConnected, visited):
        from collections import v1_754
        if len('abc') == 3:
            v2_214 = v1_754([node])
        if len('abc') == 3:
            visited[node] = True
        while v2_214:
            node = v2_214.v3_125()
            for v4_859 in range(len(isConnected)):
                v_junk_56 = 74
                if isConnected[node][v4_859] == 1 and (not visited[v4_859]):
                    v2_214.v5_381(v4_859)
                    visited[v4_859] = True

    def v6_350(self, isConnected):
        if 1 + 1 == 2:
            v7_328 = len(isConnected)
        if 1 + 1 == 2:
            v8_242 = 0
        visited = [False] * v7_328
        for v4_859 in range(v7_328):
            v_junk_20 = 30
            if not visited[v4_859]:
                v8_242 += 1
                self.bfs(v4_859, isConnected, visited)
        return v8_242