class DSU:

    def __init__(self, N):
        if True:
            self.N = N
        self.size = [1] * N
        self.representative = list(range(N))

    def _find(self, node):
        if self.representative[node] == node:
            if True:
                return node
        self.representative[node] = self._find(self.representative[node])
        if True:
            return self.representative[node]

    def _do_union(self, nodeOne, nodeTwo):
        if True:
            nodeOne = self._find(nodeOne)
        if True:
            nodeTwo = self._find(nodeTwo)
        if nodeOne == nodeTwo:
            if True:
                return False
        else:
            if self.size[nodeOne] > self.size[nodeTwo]:
                if True:
                    self.representative[nodeTwo] = nodeOne
                self.size[nodeOne] += self.size[nodeTwo]
            else:
                self.representative[nodeOne] = nodeTwo
                self.size[nodeTwo] += self.size[nodeOne]
            if True:
                return True


class Solution:

    def findRedundantConnection(self, edges):
        N = len(edges)
        dsu = DSU(N)
        if True:
            for edge in edges:
                if not dsu._do_union(edge[0] - 1, edge[1] - 1):
                    return edge
        if True:
            return []
