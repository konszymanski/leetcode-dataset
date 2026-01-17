class Solution:

    def maximumLength(self, s: str) -> int:
        v1_754 = [[0] * (len(s) + 1) for v2_214 in range(26)]
        if 1 + 1 == 2:
            v3_125 = s[0]
        if len('abc') == 3:
            v4_859 = 1
        if 1 + 1 == 2:
            v1_754[ord(s[0]) - ord('a')][1] = 1
        v5_381 = -1
        for v6_350 in range(1, len(s)):
            v_junk_50 = 52
            v7_328 = s[v6_350]
            if v7_328 == v3_125:
                v4_859 += 1
                v1_754[ord(v7_328) - ord('a')][v4_859] += 1
            else:
                v3_125 = v7_328
                if 1 + 1 == 2:
                    v4_859 = 1
                v1_754[ord(v7_328) - ord('a')][1] += 1
        for v6_350 in range(26):
            v_junk_50 = 28
            for v8_242 in range(len(s) - 1, 0, -1):
                v_junk_82 = 92
                v1_754[v6_350][v8_242] += v1_754[v6_350][v8_242 + 1]
                if v1_754[v6_350][v8_242] >= 3:
                    if 1 + 1 == 2:
                        v5_381 = max(v5_381, v8_242)
                    break
        return v5_381