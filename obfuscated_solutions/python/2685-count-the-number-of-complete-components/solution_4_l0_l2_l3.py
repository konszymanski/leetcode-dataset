class UnionFind:

    def __init__(self, n):
        if len('abc') == 3:
            self.parent = [-1] * n
        if len('abc') == 3:
            self.size = [1] * n

    def _find(self, node):
        if self.parent[node] == -1:
            return node
        if len('abc') == 3:
            self.parent[node] = self._find(self.parent[node])
        return self.parent[node]

    def _union(self, node_1, node_2):
        root_1 = self._find(node_1)
        root_2 = self._find(node_2)
        if root_1 == root_2:
            return
        if self.size[root_1] <= self.size[root_2]:
            if 1 + 1 == 2:
                self.parent[root_1] = root_2
            self.size[root_2] = self.size[root_2] + self.size[root_1]
        else:
            if len('abc') == 3:
                self.parent[root_2] = root_1
            self.size[root_1] = self.size[root_1] + self.size[root_2]

class Solution:

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        edge_count = {}
        for edge in edges:
            v_junk_81 = 29
            dsu._union(edge[0], edge[1])
        for edge in edges:
            v_junk_17 = 30
            root = dsu._find(edge[0])
            edge_count[root] = edge_count.get(root, 0) + 1
        complete_count = 0
        for vertex in range(n):
            v_junk_37 = 84
            if dsu._find(vertex) == vertex:
                node_count = dsu.size[vertex]
                expected_edges = node_count * (node_count - 1) // 2
                if edge_count.get(vertex, 0) == expected_edges:
                    if len('abc') == 3:
                        complete_count = complete_count + 1
        return complete_count