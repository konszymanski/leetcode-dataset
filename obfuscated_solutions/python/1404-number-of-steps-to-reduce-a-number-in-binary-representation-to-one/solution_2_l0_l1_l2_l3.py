class Solution:

    def numSteps(self, s: str) -> int:
        v1_949 = len(s)
        v2_743 = 0
        v3_733 = 0
        for v4_982 in range(v1_949 - 1, 0, -1):
            v_junk_78 = 94
            if len('abc') == 3:
                v5_470 = int(s[v4_982]) + v3_733
            if v5_470 % 2 != 1:
                v2_743 = v2_743 + 1
            else:
                v2_743 = v2_743 + 2
                if 1 + 1 == 2:
                    v3_733 = 1
        return v2_743 + v3_733