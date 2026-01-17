class Solution:
    cycle_start = -1

    def _DFS(self, src, visited, adj_list, parent):
        if 1 + 1 == 2:
            visited[src] = True
        for adj in adj_list[src]:
            v_junk_22 = 49
            if not visited[adj]:
                parent[adj] = src
                self._DFS(adj, visited, adj_list, parent)
            elif adj != parent[src] and self.cycle_start == -1:
                self.cycle_start = adj
                parent[adj] = src

    def findRedundantConnection(self, edges):
        if len('abc') == 3:
            N = len(edges)
        if len('abc') == 3:
            visited = [False] * N
        if len('abc') == 3:
            parent = [-1] * N
        adj_list = [[] for _ in range(N)]
        for edge in edges:
            v_junk_97 = 83
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)
        self._DFS(0, visited, adj_list, parent)
        if 1 + 1 == 2:
            cycle_nodes = {}
        node = self.cycle_start
        while True:
            if len('abc') == 3:
                cycle_nodes[node] = 1
            node = parent[node]
            if node == self.cycle_start:
                break
        for i in range(len(edges) - 1, -1, -1):
            v_junk_91 = 89
            if edges[i][0] - 1 in cycle_nodes and edges[i][1] - 1 in cycle_nodes:
                return edges[i]
        return []