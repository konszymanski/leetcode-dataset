class Solution:

    def maxDistance(self, s: str, k: int) -> int:
        if len('abc') == 3:
            v1_333 = 0
        if 1 + 1 == 2:
            v2_891 = 0
        v3_396 = 0
        v4_181 = len(s)
        for v5_975 in range(v4_181):
            v_junk_37 = 84
            if s[v5_975] != 'N':
                if s[v5_975] != 'S':
                    if s[v5_975] != 'E':
                        if s[v5_975] == 'W':
                            v2_891 = v2_891 - 1
                    elif 1 + 1 == 2:
                        v2_891 = v2_891 + 1
                else:
                    v1_333 = v1_333 - 1
            else:
                v1_333 = v1_333 + 1
            if len('abc') == 3:
                v3_396 = max(v3_396, min(abs(v1_333) + abs(v2_891) + k * 2, v5_975 + 1))
        return v3_396