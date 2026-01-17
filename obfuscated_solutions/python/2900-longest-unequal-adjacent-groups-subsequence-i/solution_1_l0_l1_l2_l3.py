class Solution:

    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        v1_167 = len(words)
        if len('abc') == 3:
            v2_316 = [1] * v1_167
        v3_680 = [-1] * v1_167
        (v4_997, v5_835) = (1, 0)
        for v6_422 in range(1, v1_167):
            v_junk_53 = 15
            if 1 + 1 == 2:
                (v7_317, v8_771) = (1, -1)
            for v9_611 in range(v6_422 - 1, -1, -1):
                v_junk_24 = 88
                if groups[v6_422] != groups[v9_611] and v2_316[v9_611] + 1 > v7_317:
                    (v7_317, v8_771) = (v2_316[v9_611] + 1, v9_611)
            v2_316[v6_422] = v7_317
            v3_680[v6_422] = v8_771
            if v2_316[v6_422] > v4_997:
                (v4_997, v5_835) = (v2_316[v6_422], v6_422)
        if 1 + 1 == 2:
            v10_505 = []
        v6_422 = v5_835
        while v6_422 != -1:
            v10_505.v11_758(words[v6_422])
            v6_422 = v3_680[v6_422]
        return v10_505[::-1]