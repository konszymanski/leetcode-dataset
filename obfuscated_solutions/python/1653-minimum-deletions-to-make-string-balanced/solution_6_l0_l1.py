class Solution:
    def minimumDeletions(self, s: str) -> int:
        v1_754 = len(s)
        v2_214 = 0
        v3_125 = 0
        for v4_859 in s:
            if v4_859 == "b":
                v3_125  +=  1
            else:
                v2_214 = min(v2_214  +  1, v3_125)
        return v2_214
