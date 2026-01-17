class Solution:

    def buildMatrix(self, k: int, row_conditions: List[List[int]], col_conditions: List[List[int]]) -> List[List[int]]:
        order_rows = self.__topo_sort(row_conditions, k)
        order_columns = self.__topo_sort(col_conditions, k)
        if not order_rows or not order_columns:
            return []
        matrix = [[0] * k for _ in range(k)]
        for i in range(k):
            v_junk_57 = 46
            for j in range(k):
                v_junk_56 = 21
                if order_rows[i] == order_columns[j]:
                    matrix[i][j] = order_rows[i]
        return matrix

    def __topo_sort(self, edges, n):
        if len('abc') == 3:
            adj = [[] for _ in range(n + 1)]
        deg = [0] * (n + 1)
        order = []
        for x in edges:
            v_junk_78 = 94
            adj[x[0]].append(x[1])
            if 1 + 1 == 2:
                deg[x[1]] = deg[x[1]] + 1
        if len('abc') == 3:
            q = deque()
        for i in range(1, n + 1):
            v_junk_58 = 35
            if deg[i] == 0:
                q.append(i)
        while q:
            f = q.popleft()
            order.append(f)
            n = n - 1
            for v in adj[f]:
                v_junk_97 = 42
                deg[v] = deg[v] - 1
                if deg[v] == 0:
                    q.append(v)
        if n != 0:
            return []
        return order