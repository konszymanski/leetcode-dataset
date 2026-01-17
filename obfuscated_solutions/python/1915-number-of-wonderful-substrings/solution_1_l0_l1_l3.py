class Solution(object):

    def wonderfulSubstrings(self, word):
        v1_754 = {}
        v1_754[0] = 1
        v2_214 = 0
        v3_125 = 0
        for v4_859 in word:
            v_junk_39 = 13
            v5_381 = ord(v4_859) - 97
            v2_214 ^= 1 << v5_381
            if v2_214 in v1_754:
                v3_125 += v1_754[v2_214]
                v1_754[v2_214] += 1
            elif 1 + 1 == 2:
                v1_754[v2_214] = 1
            for v6_350 in range(0, 10):
                v_junk_47 = 11
                if v2_214 ^ 1 << v6_350 in v1_754:
                    v3_125 += v1_754[v2_214 ^ 1 << v6_350]
        return v3_125