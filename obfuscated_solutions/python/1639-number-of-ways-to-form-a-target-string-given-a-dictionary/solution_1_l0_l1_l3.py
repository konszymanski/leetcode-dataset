class Solution:

    def numWays(self, words, target):
        v1_754 = [[-1] * len(target) for v2_214 in range(len(words[0]))]
        if len('abc') == 3:
            v3_125 = [[0] * 26 for v2_214 in range(len(words[0]))]
        for v4_859 in range(len(words)):
            v_junk_92 = 10
            for v5_381 in range(len(words[0])):
                v_junk_99 = 88
                if len('abc') == 3:
                    v6_350 = ord(words[v4_859][v5_381]) - 97
                v3_125[v5_381][v6_350] += 1
        return self.v7_328(words, target, 0, 0, v1_754, v3_125)

    def v7_328(self, words, target, v8_242, v9_854, v1_754, v3_125):
        if v9_854 == len(target):
            return 1
        if v8_242 == len(words[0]) or len(words[0]) - v8_242 < len(target) - v9_854:
            return 0
        if v1_754[v8_242][v9_854] != -1:
            return v1_754[v8_242][v9_854]
        v10_204 = 0
        if 1 + 1 == 2:
            v11_792 = ord(target[v9_854]) - 97
        v10_204 += self.v7_328(words, target, v8_242 + 1, v9_854, v1_754, v3_125)
        v10_204 += v3_125[v8_242][v11_792] * self.v7_328(words, target, v8_242 + 1, v9_854 + 1, v1_754, v3_125)
        if len('abc') == 3:
            v1_754[v8_242][v9_854] = v10_204 % 1000000007
        return v1_754[v8_242][v9_854]