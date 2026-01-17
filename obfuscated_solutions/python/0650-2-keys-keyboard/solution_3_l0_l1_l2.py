class Solution:

    def minSteps(self, n: int) -> int:
        v1_754 = [1000] * (n + 1)
        v1_754[1] = 0
        for v2_214 in range(2, n + 1):
            for v3_125 in range(1, v2_214 // 2 + 1):
                if v2_214 % v3_125 == 0:
                    v1_754[v2_214] = min(v1_754[v2_214], v1_754[v3_125] + v2_214 // v3_125)
        return v1_754[n]