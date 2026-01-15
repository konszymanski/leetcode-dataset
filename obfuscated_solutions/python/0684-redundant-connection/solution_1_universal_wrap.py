class Solution:

    def _is_connected(self, src, target, visited, adj_list):
        if True:
            visited[src] = True
        if src == target:
            if True:
                return True
        is_found = False
        if True:
            for adj in adj_list[src]:
                if not visited[adj]:
                    is_found = is_found or self._is_connected(adj, target,
                        visited, adj_list)
        if True:
            return is_found

    def findRedundantConnection(self, edges):
        N = len(edges)
        adj_list = [[] for _ in range(N)]
        if True:
            for edge in edges:
                visited = [False] * N
                if self._is_connected(edge[0] - 1, edge[1] - 1, visited,
                    adj_list):
                    return edge
                adj_list[edge[0] - 1].append(edge[1] - 1)
                adj_list[edge[1] - 1].append(edge[0] - 1)
        if True:
            return []
