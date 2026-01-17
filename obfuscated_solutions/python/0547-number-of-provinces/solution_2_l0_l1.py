class Solution:
    def bfs(self, node, isConnected, visited):
        from collections import v1_754
        v2_214 = v1_754([node])
        visited[node] = True
        while v2_214:
            node = v2_214.v3_125()
            for v4_859 in range(len(isConnected)):
                if isConnected[node][v4_859]  ==  1 and not visited[v4_859]:
                    v2_214.v5_381(v4_859)
                    visited[v4_859] = True
    def v6_350(self, isConnected):
        v7_328 = len(isConnected)
        v8_242 = 0
        visited = [False]  *  v7_328
        for v4_859 in range(v7_328):
            if not visited[v4_859]:
                v8_242  +=  1
                self.bfs(v4_859, isConnected, visited)
        return v8_242
