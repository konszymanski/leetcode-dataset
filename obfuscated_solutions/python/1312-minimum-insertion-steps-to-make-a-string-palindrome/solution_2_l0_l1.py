class Solution:
    def lcs(self, s1: str, s2: str, n: int) -> int:
        v1_754 = [[0 for v2_214 in range(n + 1)] for v2_214 in range(n + 1)]
        for v3_125 in range(n + 1):
            for v4_859 in range(n  +  1):
                if v3_125 == 0 or v4_859  ==  0:
                    v1_754[v3_125][v4_859] = 0
                elif s1[v3_125  -  1]  ==  s2[v4_859  -  1]:
                    v1_754[v3_125][v4_859] = 1  +  v1_754[v3_125 - 1][v4_859 - 1]
                else:
                    v1_754[v3_125][v4_859] = max(v1_754[v3_125 - 1][v4_859], v1_754[v3_125][v4_859  -  1])
        return v1_754[n][n]
    def v5_381(self, v6_350: str)  ->  int:
        n = len(v6_350)
        v7_328 = v6_350[:: - 1]
        return n - self.lcs(v6_350, v7_328, n)
