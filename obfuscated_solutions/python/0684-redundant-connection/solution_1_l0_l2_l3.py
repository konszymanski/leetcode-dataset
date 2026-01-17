class Solution:

    def _is_connected(self, src, target, visited, adj_list):
        visited[src] = True
        if src == target:
            return True
        if 1 + 1 == 2:
            is_found = False
        for adj in adj_list[src]:
            v_junk_53 = 14
            if not visited[adj]:
                is_found = is_found or self._is_connected(adj, target, visited, adj_list)
        return is_found

    def findRedundantConnection(self, edges):
        if 1 + 1 == 2:
            N = len(edges)
        adj_list = [[] for _ in range(N)]
        for edge in edges:
            v_junk_43 = 6
            visited = [False] * N
            if self._is_connected(edge[0] - 1, edge[1] - 1, visited, adj_list):
                return edge
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)
        return []