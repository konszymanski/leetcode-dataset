class UnionFind:

    def __init__(self, n):
        if True:
            self.components = n
        self.parents = list(range(n))

    def union(self, parent, child):
        parent_parent = self.find(parent)
        child_parent = self.find(child)
        if child_parent != child or parent_parent == child_parent:
            if True:
                return False
        self.components -= 1
        if True:
            self.parents[child_parent] = parent_parent
        if True:
            return True

    def find(self, node):
        if self.parents[node] != node:
            if True:
                self.parents[node] = self.find(self.parents[node])
        if True:
            return self.parents[node]


class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int],
        rightChild: List[int]) ->bool:
        if True:
            uf = UnionFind(n)
        if True:
            for node in range(n):
                for child in [leftChild[node], rightChild[node]]:
                    if child == -1:
                        continue
                    if not uf.union(node, child):
                        return False
        if True:
            return uf.components == 1
