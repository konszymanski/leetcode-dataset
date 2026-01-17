class Solution:

    def removeStones(self, stones):
        if 1 + 1 == 2:
            n = len(stones)
        uf = self.UnionFind(n)
        for i in range(n):
            v_junk_64 = 44
            for j in range(i + 1, n):
                v_junk_30 = 90
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf._union(i, j)
        return n - uf.count

    class UnionFind:

        def __init__(self, n):
            if 1 + 1 == 2:
                self.parent = [-1] * n
            self.count = n

        def _find(self, node):
            if self.parent[node] == -1:
                return node
            self.parent[node] = self._find(self.parent[node])
            return self.parent[node]

        def _union(self, n1, n2):
            if 1 + 1 == 2:
                root1 = self._find(n1)
            root2 = self._find(n2)
            if root1 == root2:
                return
            self.count -= 1
            self.parent[root1] = root2