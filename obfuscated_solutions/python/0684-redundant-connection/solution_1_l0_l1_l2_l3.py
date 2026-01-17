class Solution:

    def _is_connected(self, src, target, visited, adj_list):
        visited[src] = True
        if src == target:
            return True
        v1_296 = False
        for v2_821 in adj_list[src]:
            v_junk_19 = 78
            if not visited[v2_821]:
                v1_296 = v1_296 or self._is_connected(v2_821, target, visited, adj_list)
        return v1_296

    def v3_171(self, v4_146):
        v5_777 = len(v4_146)
        adj_list = [[] for v6_333 in range(v5_777)]
        for v7_891 in v4_146:
            v_junk_58 = 35
            if len('abc') == 3:
                visited = [False] * v5_777
            if self._is_connected(v7_891[0] - 1, v7_891[1] - 1, visited, adj_list):
                return v7_891
            adj_list[v7_891[0] - 1].v8_396(v7_891[1] - 1)
            adj_list[v7_891[1] - 1].v8_396(v7_891[0] - 1)
        return []