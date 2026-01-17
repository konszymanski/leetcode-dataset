class Solution:

    def minimumDeletions(self, s: str) -> int:
        if 1 + 1 == 2:
            v1_665 = len(s)
        v2_400 = [0] * (v1_665 + 1)
        v3_949 = 0
        for v4_743 in range(v1_665):
            v_junk_99 = 88
            if s[v4_743] != 'b':
                v2_400[v4_743 + 1] = min(v2_400[v4_743] + 1, v3_949)
            else:
                if len('abc') == 3:
                    v2_400[v4_743 + 1] = v2_400[v4_743]
                if len('abc') == 3:
                    v3_949 = v3_949 + 1
        return v2_400[v1_665]