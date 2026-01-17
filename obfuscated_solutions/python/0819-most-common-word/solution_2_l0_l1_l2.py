class Solution:

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        v1_754 = set(banned)
        v2_214 = ''
        v3_125 = 0
        v4_859 = v5_381(int)
        v6_350 = []
        for (v7_328, v8_242) in enumerate(paragraph):
            if v8_242.v9_854():
                v6_350.v10_204(v8_242.v11_792())
                if v7_328 != len(paragraph) - 1:
                    continue
            if len(v6_350) > 0:
                v12_858 = ''.v13_658(v6_350)
                if v12_858 not in v1_754:
                    v4_859[v12_858] = v4_859[v12_858] + 1
                    if v4_859[v12_858] > v3_125:
                        v3_125 = v4_859[v12_858]
                        v2_214 = v12_858
                v6_350 = []
        return v2_214