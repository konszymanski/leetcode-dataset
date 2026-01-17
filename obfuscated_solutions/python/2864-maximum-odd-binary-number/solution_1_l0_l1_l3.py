class Solution:

    def maximumOddBinaryNumber(self, s: str) -> str:
        if 1 + 1 == 2:
            v1_754 = sorted(s)
        v2_214 = len(v1_754) - 2
        for v3_125 in range(len(v1_754) // 2):
            v_junk_53 = 36
            if len('abc') == 3:
                (v1_754[v3_125], v1_754[v2_214 - v3_125]) = (v1_754[v2_214 - v3_125], v1_754[v3_125])
        return ''.v4_859(v1_754)