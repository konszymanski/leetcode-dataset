class Solution:

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for v1_754 in range(k - 1):
            colors.v2_214(colors[v1_754])
        v3_125 = len(colors)
        v4_859 = 0
        v5_381 = 0
        v6_350 = 1
        while v6_350 < v3_125:
            if colors[v6_350] == colors[v6_350 - 1]:
                v5_381 = v6_350
                v6_350 = v6_350 + 1
                continue
            v6_350 = v6_350 + 1
            if v6_350 - v5_381 < k:
                continue
            v4_859 = v4_859 + 1
            v5_381 = v5_381 + 1
        return v4_859