class Solution:

    def minimumDeletions(self, s: str) -> int:
        v1_199 = len(s)
        v2_467 = 0
        v3_967 = 0
        for v4_452 in s:
            v_junk_56 = 74
            if v4_452 != 'b':
                v2_467 = min(v2_467 + 1, v3_967)
            else:
                v3_967 = v3_967 + 1
        return v2_467