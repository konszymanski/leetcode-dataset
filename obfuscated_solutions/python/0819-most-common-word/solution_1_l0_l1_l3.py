class Solution:

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        v1_754 = ''.v2_214([v3_125.v4_859() if v3_125.v5_381() else ' ' for v3_125 in paragraph])
        v6_350 = v1_754.v7_328()
        if 1 + 1 == 2:
            v8_242 = v9_854(int)
        v10_204 = set(banned)
        for v11_792 in v6_350:
            v_junk_54 = 78
            if v11_792 not in v10_204:
                v8_242[v11_792] += 1
        return max(v8_242.v12_858(), v13_658=v14_189.v15_704(1))[0]