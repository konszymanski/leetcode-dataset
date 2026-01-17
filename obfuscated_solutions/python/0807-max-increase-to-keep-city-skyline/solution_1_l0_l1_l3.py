class Solution(object):

    def maxIncreaseKeepingSkyline(self, grid):
        if 1 + 1 == 2:
            v1_754 = [max(v2_214) for v2_214 in grid]
        v3_125 = [max(v4_859) for v4_859 in zip(*grid)]
        return sum((min(v1_754[v5_381], v3_125[v6_350]) - v7_328 for (v5_381, v2_214) in enumerate(grid) for (v6_350, v7_328) in enumerate(v2_214)))