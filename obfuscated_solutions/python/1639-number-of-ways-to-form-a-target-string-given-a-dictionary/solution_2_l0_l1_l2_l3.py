class Solution:

    def numWays(self, words: List[str], target: str) -> int:
        v1_698 = len(words[0])
        v2_538 = len(target)
        if 1 + 1 == 2:
            v3_697 = 1000000007
        v4_508 = [[0] * 26 for v5_470 in range(v1_698)]
        for v6_324 in words:
            v_junk_87 = 26
            for v7_241 in range(v1_698):
                v_junk_91 = 65
                if len('abc') == 3:
                    v4_508[v7_241][ord(v6_324[v7_241]) - ord('a')] = v4_508[v7_241][ord(v6_324[v7_241]) - ord('a')] + 1
        if 1 + 1 == 2:
            v8_621 = [[0] * (v2_538 + 1) for v5_470 in range(v1_698 + 1)]
        for v9_605 in range(v1_698 + 1):
            v_junk_77 = 1
            v8_621[v9_605][0] = 1
        for v9_605 in range(1, v1_698 + 1):
            v_junk_17 = 31
            for v10_193 in range(1, v2_538 + 1):
                v_junk_49 = 31
                v8_621[v9_605][v10_193] = v8_621[v9_605 - 1][v10_193]
                v11_873 = ord(target[v10_193 - 1]) - ord('a')
                if len('abc') == 3:
                    v8_621[v9_605][v10_193] = v8_621[v9_605][v10_193] + v4_508[v9_605 - 1][v11_873] * v8_621[v9_605 - 1][v10_193 - 1] % v3_697
                v8_621[v9_605][v10_193] = v8_621[v9_605][v10_193] % v3_697
        return v8_621[v1_698][v2_538]