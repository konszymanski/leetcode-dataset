class Solution:

    def minimumDeletions(self, s: str) -> int:
        v1_754 = len(s)
        v2_214 = sum((1 for v3_125 in s if v3_125 == 'a'))
        v4_859 = 0
        v5_381 = v1_754
        for v3_125 in s:
            if v3_125 == 'a':
                v2_214 = v2_214 - 1
            v5_381 = min(v5_381, v2_214 + v4_859)
            if v3_125 == 'b':
                v4_859 = v4_859 + 1
        return v5_381