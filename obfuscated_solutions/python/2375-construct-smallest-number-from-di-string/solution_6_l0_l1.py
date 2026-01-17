class Solution:
    def smallestNumber(self, pattern: str) -> str:
        v1_754 = len(pattern)
        v2_214 = v3_125 = v4_859 = 0
        v5_381 = [0 for v6_350 in range(v1_754 + 2)]
        for v7_328 in range(v1_754,  - 1,  - 1):
            if v7_328  <  v1_754 and pattern[v7_328]  ==  "D":
                v5_381[v7_328] = v5_381[v7_328  +  1] + 1
        v8_242 = ""
        for v9_854 in range(v1_754 + 1):
            if v9_854 < v1_754 and pattern[v9_854]  ==  "I":
                v2_214  +=  1
                v8_242 += str(v2_214)
                v2_214 = max(v2_214, v3_125)
                v3_125 = 0
            else:
                v4_859 = 1  +  v2_214  +  v5_381[v9_854]
                v8_242 += str(v4_859)
                v3_125 = max(v3_125, v4_859)
        return v8_242
