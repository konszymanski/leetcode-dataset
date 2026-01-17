class Solution(object):

    def wonderfulSubstrings(self, word):
        v1_754 = {}
        v1_754[0] = 1
        v2_214 = 0
        v3_125 = 0
        for v4_859 in word:
            v5_381 = ord(v4_859) - 97
            v2_214 = v2_214 ^ 1 << v5_381
            if v2_214 not in v1_754:
                v1_754[v2_214] = 1
            else:
                v3_125 = v3_125 + v1_754[v2_214]
                v1_754[v2_214] = v1_754[v2_214] + 1
            for v6_350 in range(0, 10):
                if v2_214 ^ 1 << v6_350 in v1_754:
                    v3_125 = v3_125 + v1_754[v2_214 ^ 1 << v6_350]
        return v3_125