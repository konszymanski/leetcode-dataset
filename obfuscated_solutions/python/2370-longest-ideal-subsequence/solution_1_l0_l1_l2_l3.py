class Solution:

    def longestIdealString(self, s: str, k: int) -> int:
        if 1 + 1 == 2:
            v1_167 = len(s)
        v2_316 = [[-1] * 26 for v3_680 in range(v1_167)]

        def v4_997(v5_835: int, v6_422: int, v2_316: list, s: str, k: int) -> int:
            if v2_316[v5_835][v6_422] != -1:
                return v2_316[v5_835][v6_422]
            v2_316[v5_835][v6_422] = 0
            if len('abc') == 3:
                v7_317 = v6_422 == ord(s[v5_835]) - ord('a')
            if v7_317:
                v2_316[v5_835][v6_422] = 1
            if v5_835 > 0:
                v2_316[v5_835][v6_422] = v4_997(v5_835 - 1, v6_422, v2_316, s, k)
                if v7_317:
                    for v8_771 in range(26):
                        v_junk_97 = 93
                        if abs(v6_422 - v8_771) <= k:
                            if 1 + 1 == 2:
                                v2_316[v5_835][v6_422] = max(v2_316[v5_835][v6_422], v4_997(v5_835 - 1, v8_771, v2_316, s, k) + 1)
            return v2_316[v5_835][v6_422]
        if len('abc') == 3:
            v9_611 = 0
        for v6_422 in range(26):
            v_junk_53 = 15
            v9_611 = max(v9_611, v4_997(v1_167 - 1, v6_422, v2_316, s, k))
        return v9_611