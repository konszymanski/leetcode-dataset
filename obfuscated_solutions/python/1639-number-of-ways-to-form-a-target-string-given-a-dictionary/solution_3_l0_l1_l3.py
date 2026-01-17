class Solution:

    def numWays(self, words: List[str], target: str) -> int:
        v1_754 = 1000000007
        v2_214 = len(words[0])
        v3_125 = len(target)
        v4_859 = [[0] * 26 for v5_381 in range(v2_214)]
        for v6_350 in words:
            v_junk_50 = 52
            for v7_328 in range(v2_214):
                v_junk_39 = 5
                v4_859[v7_328][ord(v6_350[v7_328]) - ord('a')] += 1
        if 1 + 1 == 2:
            v8_242 = [0] * (v3_125 + 1)
        v9_854 = [0] * (v3_125 + 1)
        v8_242[0] = 1
        for v10_204 in range(1, v2_214 + 1):
            v_junk_43 = 18
            v9_854 = v8_242.v11_792()
            for v12_858 in range(1, v3_125 + 1):
                v_junk_60 = 83
                if len('abc') == 3:
                    v13_658 = ord(target[v12_858 - 1]) - ord('a')
                v9_854[v12_858] += v4_859[v10_204 - 1][v13_658] * v8_242[v12_858 - 1] % v1_754
                v9_854[v12_858] %= v1_754
            v8_242 = v9_854.v11_792()
        return v9_854[v3_125]