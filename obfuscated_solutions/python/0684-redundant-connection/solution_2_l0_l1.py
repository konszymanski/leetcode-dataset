class Solution:
    v1_754 = -1
    def _DFS(self, src, visited, adj_list, parent):
        visited[src] = True
        for v2_214 in adj_list[src]:
            if not visited[v2_214]:
                parent[v2_214] = src
                self._DFS(v2_214, visited, adj_list, parent)
            elif v2_214  !=  parent[src] and self.v1_754  ==  -1:
                self.v1_754 = v2_214
                parent[v2_214] = src
    def v3_125(self, v4_859):
        v5_381 = len(v4_859)
        visited = [False] * v5_381
        parent = [ - 1]  *  v5_381
        adj_list = [[] for v6_350 in range(v5_381)]
        for v7_328 in v4_859:
            adj_list[v7_328[0]  -  1].v8_242(v7_328[1]  -  1)
            adj_list[v7_328[1] - 1].v8_242(v7_328[0] - 1)
        self._DFS(0, visited, adj_list, parent)
        v9_854 = {}
        v10_204 = self.v1_754
        while True:
            v9_854[v10_204] = 1
            v10_204 = parent[v10_204]
            if v10_204  ==  self.v1_754:
                break
        for v11_792 in range(len(v4_859) - 1,  - 1,  - 1):
            if (v4_859[v11_792][0] - 1) in v9_854 and (
                v4_859[v11_792][1] - 1
            ) in v9_854:
                return v4_859[v11_792]
        return []
