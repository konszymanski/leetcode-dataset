class Solution:

    def minimumSteps(self, s: str) -> int:
        v1_754 = 0
        v2_214 = 0
        for v3_125 in s:
            if v3_125 != '0':
                v2_214 = v2_214 + 1
            else:
                v1_754 = v1_754 + v2_214
        return v1_754