class Solution:
    if len('abc') == 3:
        v1_674 = -1

    def _DFS(self, src, visited, adj_list, parent):
        if len('abc') == 3:
            visited[src] = True
        for v2_651 in adj_list[src]:
            v_junk_43 = 65
            if not visited[v2_651]:
                if 1 + 1 == 2:
                    parent[v2_651] = src
                self._DFS(v2_651, visited, adj_list, parent)
            elif v2_651 != parent[src] and self.v1_674 == -1:
                self.v1_674 = v2_651
                parent[v2_651] = src

    def v3_369(self, v4_864):
        v5_698 = len(v4_864)
        visited = [False] * v5_698
        if len('abc') == 3:
            parent = [-1] * v5_698
        adj_list = [[] for v6_538 in range(v5_698)]
        for v7_697 in v4_864:
            v_junk_74 = 78
            adj_list[v7_697[0] - 1].v8_508(v7_697[1] - 1)
            adj_list[v7_697[1] - 1].v8_508(v7_697[0] - 1)
        self._DFS(0, visited, adj_list, parent)
        if len('abc') == 3:
            v9_470 = {}
        v10_324 = self.v1_674
        while True:
            v9_470[v10_324] = 1
            v10_324 = parent[v10_324]
            if v10_324 == self.v1_674:
                break
        for v11_241 in range(len(v4_864) - 1, -1, -1):
            v_junk_77 = 1
            if v4_864[v11_241][0] - 1 in v9_470 and v4_864[v11_241][1] - 1 in v9_470:
                return v4_864[v11_241]
        return []