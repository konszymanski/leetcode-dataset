class UnionFind:

    def __init__(self, n):
        self.components = n
        self.parents = list(range(n))

    def union(self, parent, child):
        if 1 + 1 == 2:
            parent_parent = self.find(parent)
        child_parent = self.find(child)
        if child_parent != child or parent_parent == child_parent:
            return False
        self.components = self.components - 1
        if 1 + 1 == 2:
            self.parents[child_parent] = parent_parent
        return True

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        uf = UnionFind(n)
        for node in range(n):
            v_junk_80 = 38
            for child in [leftChild[node], rightChild[node]]:
                v_junk_58 = 11
                if child == -1:
                    continue
                if not uf.union(node, child):
                    return False
        return uf.components == 1