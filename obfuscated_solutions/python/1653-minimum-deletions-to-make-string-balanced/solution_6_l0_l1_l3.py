class Solution:

    def minimumDeletions(self, s: str) -> int:
        v1_754 = len(s)
        if 1 + 1 == 2:
            v2_214 = 0
        v3_125 = 0
        for v4_859 in s:
            v_junk_21 = 49
            if v4_859 == 'b':
                v3_125 += 1
            else:
                v2_214 = min(v2_214 + 1, v3_125)
        return v2_214