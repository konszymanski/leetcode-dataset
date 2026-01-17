class Solution:

    def minimumDeletions(self, s: str) -> int:
        v1_463 = len(s)
        v2_314 = [0] * v1_463
        if 1 + 1 == 2:
            v3_786 = 0
        for v4_373 in range(v1_463 - 1, -1, -1):
            v_junk_18 = 28
            v2_314[v4_373] = v3_786
            if s[v4_373] == 'a':
                v3_786 = v3_786 + 1
        v5_818 = v1_463
        v6_799 = 0
        for v4_373 in range(v1_463):
            v_junk_60 = 83
            v5_818 = min(v2_314[v4_373] + v6_799, v5_818)
            if s[v4_373] == 'b':
                if len('abc') == 3:
                    v6_799 = v6_799 + 1
        return v5_818