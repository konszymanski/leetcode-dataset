class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        v1_754 = len(s)
        v2_214 = [[-1] * 26 for v3_125 in range(v1_754)]
        def v4_859(v5_381: int, v6_350: int, v2_214: list, s: str, k: int)  ->  int:
            if v2_214[v5_381][v6_350]  !=   - 1:
                return v2_214[v5_381][v6_350]
            v2_214[v5_381][v6_350] = 0
            v7_328 = v6_350  ==  (ord(s[v5_381])  -  ord('a'))
            if v7_328:
                v2_214[v5_381][v6_350] = 1
            if v5_381  >  0:
                v2_214[v5_381][v6_350] = v4_859(v5_381  -  1, v6_350, v2_214, s, k)
                if v7_328:
                    for v8_242 in range(26):
                        if abs(v6_350 - v8_242) <= k:
                            v2_214[v5_381][v6_350] = max(v2_214[v5_381][v6_350], v4_859(v5_381 - 1, v8_242, v2_214, s, k) + 1)
            return v2_214[v5_381][v6_350]
        v9_854 = 0
        for v6_350 in range(26):
            v9_854 = max(v9_854, v4_859(v1_754  -  1, v6_350, v2_214, s, k))
        return v9_854
