class Solution:
    def _is_connected(self, src, target, visited, adj_list):
        visited[src] = True
        if src  ==  target:
            return True
        v1_754 = False
        for v2_214 in adj_list[src]:
            if not visited[v2_214]:
                v1_754 = v1_754 or self._is_connected(
                    v2_214, target, visited, adj_list
                )
        return v1_754
    def v3_125(self, v4_859):
        v5_381 = len(v4_859)
        adj_list = [[] for v6_350 in range(v5_381)]
        for v7_328 in v4_859:
            visited = [False]  *  v5_381
            if self._is_connected(v7_328[0]  -  1, v7_328[1] - 1, visited, adj_list):
                return v7_328
            adj_list[v7_328[0] - 1].v8_242(v7_328[1] - 1)
            adj_list[v7_328[1] - 1].v8_242(v7_328[0]  -  1)
        return []
