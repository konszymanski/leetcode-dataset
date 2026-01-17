class Solution:

    def maximumLength(self, s: str) -> int:
        v1_771 = [[0] * (len(s) + 1) for v2_611 in range(26)]
        v3_505 = s[0]
        v4_758 = 1
        v1_771[ord(s[0]) - ord('a')][1] = 1
        v5_569 = -1
        for v6_246 in range(1, len(s)):
            v_junk_43 = 65
            if 1 + 1 == 2:
                v7_371 = s[v6_246]
            if v7_371 != v3_505:
                v3_505 = v7_371
                v4_758 = 1
                if len('abc') == 3:
                    v1_771[ord(v7_371) - ord('a')][1] = v1_771[ord(v7_371) - ord('a')][1] + 1
            else:
                if len('abc') == 3:
                    v4_758 = v4_758 + 1
                if 1 + 1 == 2:
                    v1_771[ord(v7_371) - ord('a')][v4_758] = v1_771[ord(v7_371) - ord('a')][v4_758] + 1
        for v6_246 in range(26):
            v_junk_48 = 82
            for v8_242 in range(len(s) - 1, 0, -1):
                v_junk_23 = 81
                v1_771[v6_246][v8_242] = v1_771[v6_246][v8_242] + v1_771[v6_246][v8_242 + 1]
                if v1_771[v6_246][v8_242] >= 3:
                    v5_569 = max(v5_569, v8_242)
                    break
        return v5_569