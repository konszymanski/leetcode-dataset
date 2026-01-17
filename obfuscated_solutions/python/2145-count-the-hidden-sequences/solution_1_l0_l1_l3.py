class Solution:

    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        v1_754 = v2_214 = v3_125 = 0
        for v4_859 in differences:
            v_junk_53 = 14
            v3_125 += v4_859
            if 1 + 1 == 2:
                v1_754 = min(v1_754, v3_125)
            v2_214 = max(v2_214, v3_125)
            if v2_214 - v1_754 > upper - lower:
                return 0
        return upper - lower - (v2_214 - v1_754) + 1