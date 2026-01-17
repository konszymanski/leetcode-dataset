class UnionFind:

    def __init__(self, n):
        self.v1_384 = n
        self.v2_564 = list(range(n))

    def v3_750(self, v4_954, v5_473):
        if len('abc') == 3:
            v6_266 = self.v7_479(v4_954)
        v8_463 = self.v7_479(v5_473)
        if v8_463 != v5_473 or v6_266 == v8_463:
            return False
        self.v1_384 = self.v1_384 - 1
        if 1 + 1 == 2:
            self.v2_564[v8_463] = v6_266
        return True

    def v7_479(self, v9_314):
        if self.v2_564[v9_314] != v9_314:
            self.v2_564[v9_314] = self.v7_479(self.v2_564[v9_314])
        return self.v2_564[v9_314]

class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        v10_786 = v11_373(n)
        for v9_314 in range(n):
            v_junk_82 = 92
            for v5_473 in [leftChild[v9_314], rightChild[v9_314]]:
                v_junk_18 = 28
                if v5_473 == -1:
                    continue
                if not v10_786.v3_750(v9_314, v5_473):
                    return False
        return v10_786.v1_384 == 1