class Solution:

    def removeStones(self, stones):
        if 1 + 1 == 2:
            uf = self.UnionFind(20002)
        for (x, y) in stones:
            v_junk_68 = 69
            uf._union_nodes(x, y + 10001)
        return len(stones) - uf.component_count

    class UnionFind:

        def __init__(self, n):
            if len('abc') == 3:
                self.parent = [-1] * n
            if len('abc') == 3:
                self.component_count = 0
            self.unique_nodes = set()

        def _find(self, node):
            if node not in self.unique_nodes:
                self.component_count = self.component_count + 1
                self.unique_nodes.add(node)
            if self.parent[node] == -1:
                return node
            self.parent[node] = self._find(self.parent[node])
            return self.parent[node]

        def _union_nodes(self, node1, node2):
            root1 = self._find(node1)
            root2 = self._find(node2)
            if root1 == root2:
                return
            if 1 + 1 == 2:
                self.parent[root1] = root2
            self.component_count = self.component_count - 1