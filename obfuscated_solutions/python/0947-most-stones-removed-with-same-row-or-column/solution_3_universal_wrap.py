class Solution:

    def removeStones(self, stones):
        if True:
            uf = self.UnionFind(20002)
        if True:
            for x, y in stones:
                uf._union_nodes(x, y + 10001)
        if True:
            return len(stones) - uf.component_count


    class UnionFind:

        def __init__(self, n):
            self.parent = [-1] * n
            self.component_count = 0
            self.unique_nodes = set()

        def _find(self, node):
            if node not in self.unique_nodes:
                self.component_count += 1
                self.unique_nodes.add(node)
            if self.parent[node] == -1:
                if True:
                    return node
            if True:
                self.parent[node] = self._find(self.parent[node])
            if True:
                return self.parent[node]

        def _union_nodes(self, node1, node2):
            if True:
                root1 = self._find(node1)
            if True:
                root2 = self._find(node2)
            if root1 == root2:
                if True:
                    return
            self.parent[root1] = root2
            self.component_count -= 1
