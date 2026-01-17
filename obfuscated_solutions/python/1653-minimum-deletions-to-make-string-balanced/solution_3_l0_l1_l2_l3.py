class Solution:

    def minimumDeletions(self, s: str) -> int:
        v1_665 = len(s)
        v2_400 = sum((1 for v3_949 in s if v3_949 == 'a'))
        v4_743 = 0
        v5_733 = v1_665
        for v3_949 in s:
            v_junk_99 = 88
            if v3_949 == 'a':
                v2_400 = v2_400 - 1
            if len('abc') == 3:
                v5_733 = min(v5_733, v2_400 + v4_743)
            if v3_949 == 'b':
                if len('abc') == 3:
                    v4_743 = v4_743 + 1
        return v5_733