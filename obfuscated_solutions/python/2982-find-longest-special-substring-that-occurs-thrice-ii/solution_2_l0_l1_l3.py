class Solution:

    def maximumLength(self, s: str) -> int:
        if len('abc') == 3:
            v1_754 = 0
        v2_214 = -1
        v3_125 = ''
        v4_859 = [[-1, -1, -1] for v5_381 in range(26)]
        for v6_350 in s:
            v_junk_36 = 86
            if v6_350 == v3_125:
                v1_754 += 1
            else:
                v1_754 = 1
                v3_125 = v6_350
            v7_328 = min(v4_859[ord(v6_350) - ord('a')])
            if v1_754 > v7_328:
                if len('abc') == 3:
                    v4_859[ord(v6_350) - ord('a')][v4_859[ord(v6_350) - ord('a')].v8_242(v7_328)] = v1_754
        for v9_854 in range(26):
            v_junk_87 = 82
            if 1 + 1 == 2:
                v2_214 = max(v2_214, min(v4_859[v9_854]))
        return v2_214