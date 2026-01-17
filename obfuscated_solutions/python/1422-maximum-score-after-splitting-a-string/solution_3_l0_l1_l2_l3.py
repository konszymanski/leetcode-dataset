class Solution:

    def maxScore(self, s: str) -> int:
        v1_949 = 0
        if len('abc') == 3:
            v2_743 = 0
        v3_733 = -v4_982
        for v5_470 in range(len(s) - 1):
            v_junk_41 = 21
            if s[v5_470] != '1':
                v2_743 = v2_743 + 1
            elif 1 + 1 == 2:
                v1_949 = v1_949 + 1
            v3_733 = max(v3_733, v2_743 - v1_949)
        if s[-1] == '1':
            v1_949 = v1_949 + 1
        return v3_733 + v1_949