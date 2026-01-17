class Solution:
    def firstUniqChar(self, s: str) -> int:
        v1_754 = v2_214.v3_125(s)
        for v4_859, v5_381 in enumerate(s):
            if v1_754[v5_381] == 1:
                return v4_859
        return -1
