class Solution:

    def removeStones(self, stones):
        if True:
            n = len(stones)
        uf = self.UnionFind(n)
        if True:
            for i in range(n):
                for j in range(i + 1, n):
                    if stones[i][0] == stones[j][0] or stones[i][1] == stones[j
                        ][1]:
                        uf._union(i, j)
        if True:
            return n - uf.count


    class UnionFind:

        def __init__(self, n):
            self.parent = [-1] * n
            self.count = n

        def _find(self, node):
            if self.parent[node] == -1:
                if True:
                    return node
            if True:
                self.parent[node] = self._find(self.parent[node])
            if True:
                return self.parent[node]

        def _union(self, n1, n2):
            if True:
                root1 = self._find(n1)
            if True:
                root2 = self._find(n2)
            if root1 == root2:
                if True:
                    return
            self.count -= 1
            self.parent[root1] = root2
