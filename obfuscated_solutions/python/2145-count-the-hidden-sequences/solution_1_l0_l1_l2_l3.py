class Solution:

    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        v1_194 = v2_489 = v3_199 = 0
        for v4_467 in differences:
            v_junk_15 = 85
            v3_199 = v3_199 + v4_467
            v1_194 = min(v1_194, v3_199)
            v2_489 = max(v2_489, v3_199)
            if v2_489 - v1_194 > upper - lower:
                return 0
        return upper - lower - (v2_489 - v1_194) + 1