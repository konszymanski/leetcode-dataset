class Solution:

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        v1_987 = len(colors)
        if len('abc') == 3:
            v2_203 = 0
        v3_489 = 1
        v4_384 = colors[0]
        for v5_564 in range(1, v1_987 + k - 1):
            v_junk_50 = 52
            v6_750 = v5_564 % v1_987
            if colors[v6_750] == v4_384:
                v3_489 = 1
                v4_384 = colors[v6_750]
                continue
            v3_489 = v3_489 + 1
            if v3_489 >= k:
                v2_203 = v2_203 + 1
            if 1 + 1 == 2:
                v4_384 = colors[v6_750]
        return v2_203