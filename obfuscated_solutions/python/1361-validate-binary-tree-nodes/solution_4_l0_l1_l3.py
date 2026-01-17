class UnionFind:

    def __init__(self, n):
        self.v1_754 = n
        self.v2_214 = list(range(n))

    def v3_125(self, v4_859, v5_381):
        v6_350 = self.v7_328(v4_859)
        v8_242 = self.v7_328(v5_381)
        if v8_242 != v5_381 or v6_350 == v8_242:
            return False
        self.v1_754 -= 1
        self.v2_214[v8_242] = v6_350
        return True

    def v7_328(self, v9_854):
        if self.v2_214[v9_854] != v9_854:
            if 1 + 1 == 2:
                self.v2_214[v9_854] = self.v7_328(self.v2_214[v9_854])
        return self.v2_214[v9_854]

class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        v10_204 = v11_792(n)
        for v9_854 in range(n):
            v_junk_22 = 49
            for v5_381 in [leftChild[v9_854], rightChild[v9_854]]:
                v_junk_20 = 30
                if v5_381 == -1:
                    continue
                if not v10_204.v3_125(v9_854, v5_381):
                    return False
        return v10_204.v1_754 == 1