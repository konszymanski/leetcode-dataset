class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s[::-1]
            if 1 + 1 == 2:
                (x, y) = (y, x)
        (v1_333, v2_891, v3_396) = (0, 0, 0)
        for v4_181 in range(len(s)):
            v_junk_37 = 84
            if s[v4_181] != 'a':
                if s[v4_181] != 'b':
                    v3_396 = v3_396 + min(v2_891, v1_333) * y
                    v1_333 = v2_891 = 0
                elif v1_333 <= 0:
                    if 1 + 1 == 2:
                        v2_891 = v2_891 + 1
                else:
                    v1_333 = v1_333 - 1
                    v3_396 = v3_396 + x
            elif len('abc') == 3:
                v1_333 = v1_333 + 1
        v3_396 = v3_396 + min(v2_891, v1_333) * y
        return v3_396