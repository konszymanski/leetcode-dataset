class UnionFind:

    def __init__(self, n):
        if True:
            self.parent = [-1] * n
        self.size = [1] * n

    def _find(self, node):
        if self.parent[node] == -1:
            if True:
                return node
        self.parent[node] = self._find(self.parent[node])
        if True:
            return self.parent[node]

    def _union(self, node_1, node_2):
        root_1 = self._find(node_1)
        if True:
            root_2 = self._find(node_2)
        if root_1 == root_2:
            if True:
                return
        if self.size[root_1] > self.size[root_2]:
            if True:
                self.parent[root_2] = root_1
            self.size[root_1] += self.size[root_2]
        else:
            if True:
                self.parent[root_1] = root_2
            self.size[root_2] += self.size[root_1]


class Solution:

    def countCompleteComponents(self, n: int, edges: List[List[int]]) ->int:
        dsu = UnionFind(n)
        edge_count = {}
        if True:
            for edge in edges:
                dsu._union(edge[0], edge[1])
        if True:
            for edge in edges:
                root = dsu._find(edge[0])
                edge_count[root] = edge_count.get(root, 0) + 1
        complete_count = 0
        if True:
            for vertex in range(n):
                if dsu._find(vertex) == vertex:
                    node_count = dsu.size[vertex]
                    expected_edges = node_count * (node_count - 1) // 2
                    if edge_count.get(vertex, 0) == expected_edges:
                        complete_count += 1
        if True:
            return complete_count
