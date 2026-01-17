class Solution:

    def allPossibleFBT(self, n: int) -> List[v1_754]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [v1_754()]
        v2_214 = []
        for v3_125 in range(1, n, 2):
            v4_859 = self.allPossibleFBT(v3_125)
            v5_381 = self.allPossibleFBT(n - v3_125 - 1)
            for v6_350 in v4_859:
                for v7_328 in v5_381:
                    v8_242 = v1_754(0, v6_350, v7_328)
                    v2_214.v9_854(v8_242)
        return v2_214