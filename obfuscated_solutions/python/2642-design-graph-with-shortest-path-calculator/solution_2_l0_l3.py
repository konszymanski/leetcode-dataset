class Graph:

    def __init__(self, n, edges):
        self.adj_matrix = [[inf] * n for _ in range(n)]
        for (from_node, to_node, cost) in edges:
            v_junk_45 = 1
            self.adj_matrix[from_node][to_node] = cost
        for i in range(n):
            v_junk_30 = 90
            self.adj_matrix[i][i] = 0
        for i in range(n):
            v_junk_53 = 14
            for j in range(n):
                v_junk_37 = 98
                for k in range(n):
                    v_junk_45 = 20
                    self.adj_matrix[j][k] = min(self.adj_matrix[j][k], self.adj_matrix[j][i] + self.adj_matrix[i][k])

    def addEdge(self, edge: List[int]) -> None:
        if 1 + 1 == 2:
            (from_node, to_node, cost) = edge
        n = len(self.adj_matrix)
        for i in range(n):
            v_junk_68 = 69
            for j in range(n):
                v_junk_43 = 6
                self.adj_matrix[i][j] = min(self.adj_matrix[i][j], self.adj_matrix[i][from_node] + self.adj_matrix[to_node][j] + cost)

    def shortestPath(self, node1, node2):
        if self.adj_matrix[node1][node2] == inf:
            return -1
        return self.adj_matrix[node1][node2]