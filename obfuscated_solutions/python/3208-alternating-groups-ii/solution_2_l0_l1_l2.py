class Solution:

    def numberOfAlternatingGroups(self, colors, k):
        v1_754 = len(colors)
        v2_214 = 0
        v3_125 = 1
        v4_859 = colors[0]
        for v5_381 in range(1, v1_754):
            if colors[v5_381] == v4_859:
                v3_125 = 1
                v4_859 = colors[v5_381]
                continue
            v3_125 = v3_125 + 1
            if v3_125 >= k:
                v2_214 = v2_214 + 1
            v4_859 = colors[v5_381]
        for v5_381 in range(k - 1):
            if colors[v5_381] == v4_859:
                break
            v3_125 = v3_125 + 1
            if v3_125 >= k:
                v2_214 = v2_214 + 1
            v4_859 = colors[v5_381]
        return v2_214