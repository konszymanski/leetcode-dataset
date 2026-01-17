class Solution:

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        v1_754 = len(colors)
        v2_214 = 0
        v3_125 = 1
        v4_859 = colors[0]
        for v5_381 in range(1, v1_754 + k - 1):
            v6_350 = v5_381 % v1_754
            if colors[v6_350] == v4_859:
                v3_125 = 1
                v4_859 = colors[v6_350]
                continue
            v3_125 = v3_125 + 1
            if v3_125 >= k:
                v2_214 = v2_214 + 1
            v4_859 = colors[v6_350]
        return v2_214