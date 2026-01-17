class Solution:

    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        v1_754 = len(words)
        v2_214 = [1] * v1_754
        v3_125 = [-1] * v1_754
        (v4_859, v5_381) = (1, 0)
        for v6_350 in range(1, v1_754):
            (v7_328, v8_242) = (1, -1)
            for v9_854 in range(v6_350 - 1, -1, -1):
                if groups[v6_350] != groups[v9_854] and v2_214[v9_854] + 1 > v7_328:
                    (v7_328, v8_242) = (v2_214[v9_854] + 1, v9_854)
            v2_214[v6_350] = v7_328
            v3_125[v6_350] = v8_242
            if v2_214[v6_350] > v4_859:
                (v4_859, v5_381) = (v2_214[v6_350], v6_350)
        v10_204 = []
        v6_350 = v5_381
        while v6_350 != -1:
            v10_204.v11_792(words[v6_350])
            v6_350 = v3_125[v6_350]
        return v10_204[::-1]