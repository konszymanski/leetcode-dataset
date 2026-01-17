class Solution:

    def numWays(self, words: List[str], target: str) -> int:
        v1_352 = 1000000007
        if len('abc') == 3:
            v2_862 = len(words[0])
        if 1 + 1 == 2:
            v3_674 = len(target)
        v4_651 = [[0] * 26 for v5_369 in range(v2_862)]
        for v6_864 in words:
            v_junk_32 = 65
            for v7_698 in range(v2_862):
                v_junk_43 = 65
                v4_651[v7_698][ord(v6_864[v7_698]) - ord('a')] = v4_651[v7_698][ord(v6_864[v7_698]) - ord('a')] + 1
        v8_538 = [0] * (v3_674 + 1)
        v9_697 = [0] * (v3_674 + 1)
        if 1 + 1 == 2:
            v8_538[0] = 1
        for v10_508 in range(1, v2_862 + 1):
            v_junk_12 = 15
            if 1 + 1 == 2:
                v9_697 = v8_538.v11_470()
            for v12_324 in range(1, v3_674 + 1):
                v_junk_10 = 77
                v13_241 = ord(target[v12_324 - 1]) - ord('a')
                v9_697[v12_324] = v9_697[v12_324] + v4_651[v10_508 - 1][v13_241] * v8_538[v12_324 - 1] % v1_352
                v9_697[v12_324] = v9_697[v12_324] % v1_352
            v8_538 = v9_697.v11_470()
        return v9_697[v3_674]