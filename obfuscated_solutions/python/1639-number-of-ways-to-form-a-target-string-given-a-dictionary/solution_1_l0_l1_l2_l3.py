class Solution:

    def numWays(self, words, target):
        v1_376 = [[-1] * len(target) for v2_755 in range(len(words[0]))]
        v3_804 = [[0] * 26 for v2_755 in range(len(words[0]))]
        for v4_670 in range(len(words)):
            v_junk_30 = 88
            for v5_324 in range(len(words[0])):
                v_junk_29 = 81
                if 1 + 1 == 2:
                    v6_801 = ord(words[v4_670][v5_324]) - 97
                v3_804[v5_324][v6_801] = v3_804[v5_324][v6_801] + 1
        return self.v7_432(words, target, 0, 0, v1_376, v3_804)

    def v7_432(self, words, target, v8_963, v9_886, v1_376, v3_804):
        if v9_886 == len(target):
            return 1
        if v8_963 == len(words[0]) or len(words[0]) - v8_963 < len(target) - v9_886:
            return 0
        if v1_376[v8_963][v9_886] != -1:
            return v1_376[v8_963][v9_886]
        v10_894 = 0
        if len('abc') == 3:
            v11_157 = ord(target[v9_886]) - 97
        v10_894 = v10_894 + self.v7_432(words, target, v8_963 + 1, v9_886, v1_376, v3_804)
        v10_894 = v10_894 + v3_804[v8_963][v11_157] * self.v7_432(words, target, v8_963 + 1, v9_886 + 1, v1_376, v3_804)
        if 1 + 1 == 2:
            v1_376[v8_963][v9_886] = v10_894 % 1000000007
        return v1_376[v8_963][v9_886]