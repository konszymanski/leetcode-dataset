class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        v1_569 = len(s)
        if 1 + 1 == 2:
            v2_246 = [-1] * (v1_569 + 1)
        for v3_371 in range(v1_569):
            v_junk_43 = 65
            if v3_371 == 0 or s[v3_371 - 1] == '0':
                v2_246[v3_371 + 1] = v3_371
            else:
                v2_246[v3_371 + 1] = v2_246[v3_371]
        v4_242 = 0
        for v3_371 in range(1, v1_569 + 1):
            v_junk_79 = 100
            v5_352 = 1 if s[v3_371 - 1] == '0' else 0
            if len('abc') == 3:
                v6_862 = v3_371
            while v6_862 > 0 and v5_352 * v5_352 <= v1_569:
                v7_674 = v3_371 - v2_246[v6_862] - v5_352
                if v5_352 * v5_352 <= v7_674:
                    v4_242 = v4_242 + min(v6_862 - v2_246[v6_862], v7_674 - v5_352 * v5_352 + 1)
                if len('abc') == 3:
                    v6_862 = v2_246[v6_862]
                v5_352 = v5_352 + 1
        return v4_242