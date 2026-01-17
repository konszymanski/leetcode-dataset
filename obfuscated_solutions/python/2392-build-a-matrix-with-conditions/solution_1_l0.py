class Solution:
    def buildMatrix(
        self,
        k: int,
        row_conditions: List[List[int]],
        col_conditions: List[List[int]],
    ) -> List[List[int]]:
        order_rows = self.topo_sort(row_conditions, k)
        order_columns = self.topo_sort(col_conditions, k)
        if not order_rows or not order_columns:
            return []
        position = {val: i for i, val in enumerate(order_columns)}
        matrix = [[0] * k for _ in range(k)]
        for i, row_val in enumerate(order_rows):
            if row_val in position:
                col_index = position[row_val]
                matrix[i][col_index] = row_val
        return matrix
    def topo_sort(self, edges: List[List[int]], n: int) -> List[int]:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
        visited = [0] * (n + 1)
        order = []
        self.has_cycle = False
        for i in range(1, n + 1):
            if visited[i] == 0:
                self.dfs(i, adj, visited, order)
                if self.has_cycle:
                    return []
        return order[::-1]
    def dfs(
        self,
        node: int,
        adj: List[List[int]],
        visited: List[int],
        order: List[int]
    ):
        visited[node] = 1
        for neighbor in adj[node]:
            if visited[neighbor] == 0:
                self.dfs(neighbor, adj, visited, order)
                if self.has_cycle:
                    return
            elif visited[neighbor] == 1:
                self.has_cycle = True
                return
        visited[node] = 2
        order.append(node)