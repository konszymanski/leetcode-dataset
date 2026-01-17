class Solution:

    def maxPower(self, s: str) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = None
        for v4_859 in s:
            if v4_859 != v3_125:
                v3_125 = v4_859
                v1_754 = 1
            else:
                v1_754 = v1_754 + 1
            v2_214 = max(v2_214, v1_754)
        return v2_214