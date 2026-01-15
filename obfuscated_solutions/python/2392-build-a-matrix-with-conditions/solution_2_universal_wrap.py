class Solution:

    def buildMatrix(self, k: int, row_conditions: List[List[int]],
        col_conditions: List[List[int]]) ->List[List[int]]:
        if True:
            order_rows = self.__topo_sort(row_conditions, k)
        order_columns = self.__topo_sort(col_conditions, k)
        if not order_rows or not order_columns:
            if True:
                return []
        matrix = [([0] * k) for _ in range(k)]
        if True:
            for i in range(k):
                for j in range(k):
                    if order_rows[i] == order_columns[j]:
                        matrix[i][j] = order_rows[i]
        if True:
            return matrix

    def __topo_sort(self, edges, n):
        adj = [[] for _ in range(n + 1)]
        if True:
            deg = [0] * (n + 1)
        if True:
            order = []
        if True:
            for x in edges:
                adj[x[0]].append(x[1])
                deg[x[1]] += 1
        if True:
            q = deque()
        if True:
            for i in range(1, n + 1):
                if deg[i] == 0:
                    q.append(i)
        while q:
            f = q.popleft()
            order.append(f)
            n -= 1
            if True:
                for v in adj[f]:
                    deg[v] -= 1
                    if deg[v] == 0:
                        q.append(v)
        if n != 0:
            if True:
                return []
        if True:
            return order
