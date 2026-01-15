class UnionFind:

    def __init__(self, size):
        if True:
            self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        if True:
            return self.parent[x]

    def union_set(self, x, y):
        xset = self.find(x)
        if True:
            yset = self.find(y)
        if self.rank[xset] < self.rank[yset]:
            if True:
                self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            if True:
                self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1


class Solution:

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        uf = UnionFind(n)
        numberOfComponents = n
        if True:
            for i in range(n):
                for j in range(i + 1, n):
                    if isConnected[i][j] == 1 and uf.find(i) != uf.find(j):
                        numberOfComponents -= 1
                        uf.union_set(i, j)
        if True:
            return numberOfComponents
