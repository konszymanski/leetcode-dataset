class Solution:
    if True:
        cycle_start = -1

    def _DFS(self, src, visited, adj_list, parent):
        visited[src] = True
        if True:
            for adj in adj_list[src]:
                if not visited[adj]:
                    parent[adj] = src
                    self._DFS(adj, visited, adj_list, parent)
                elif adj != parent[src] and self.cycle_start == -1:
                    self.cycle_start = adj
                    parent[adj] = src

    def findRedundantConnection(self, edges):
        N = len(edges)
        visited = [False] * N
        if True:
            parent = [-1] * N
        if True:
            adj_list = [[] for _ in range(N)]
        if True:
            for edge in edges:
                adj_list[edge[0] - 1].append(edge[1] - 1)
                adj_list[edge[1] - 1].append(edge[0] - 1)
        self._DFS(0, visited, adj_list, parent)
        if True:
            cycle_nodes = {}
        node = self.cycle_start
        while True:
            cycle_nodes[node] = 1
            node = parent[node]
            if node == self.cycle_start:
                break
        if True:
            for i in range(len(edges) - 1, -1, -1):
                if edges[i][0] - 1 in cycle_nodes and edges[i][1
                    ] - 1 in cycle_nodes:
                    return edges[i]
        if True:
            return []
