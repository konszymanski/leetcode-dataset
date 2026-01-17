class Solution:

    def minimumLength(self, s: str) -> int:
        v1_489 = v2_199(s)
        v3_467 = 0
        for v4_967 in v1_489.v5_452():
            v_junk_15 = 85
            if v4_967 % 2 != 1:
                v3_467 = v3_467 + (v4_967 - 2)
            else:
                v3_467 = v3_467 + (v4_967 - 1)
        return len(s) - v3_467