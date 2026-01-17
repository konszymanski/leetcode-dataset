class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        self.n = n
        self.v1_754 = [[0] * (n  //  2 + 1) for v2_214 in range(n  +  1)]
        return 1  +  self.v3_125(1, 1)
    def v3_125(self, v4_859: int, v5_381: int)  ->  int:
        if v4_859  ==  self.n:
            return 0
        if v4_859  >  self.n:
            return 1000
        if self.v1_754[v4_859][v5_381] != 0:
            return self.v1_754[v4_859][v5_381]
        v6_350 = 1  +  self.v3_125(v4_859 + v5_381, v5_381)
        v7_328 = 2 + self.v3_125(v4_859 * 2, v4_859)
        self.v1_754[v4_859][v5_381] = min(v6_350, v7_328)
        return self.v1_754[v4_859][v5_381]
