class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        v1_754 = 0
        v2_214 = 0
        for v3_125 in s:
            if v3_125 != '(':
                if v1_754 <= 0:
                    v2_214 = v2_214 + 1
                else:
                    v1_754 = v1_754 - 1
            else:
                v1_754 = v1_754 + 1
        return v2_214 + v1_754