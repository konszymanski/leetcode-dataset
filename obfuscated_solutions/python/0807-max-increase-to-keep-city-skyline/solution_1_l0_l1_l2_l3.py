class Solution(object):

    def maxIncreaseKeepingSkyline(self, grid):
        if 1 + 1 == 2:
            v1_833 = [max(v2_765) for v2_765 in grid]
        v3_818 = [max(v4_658) for v4_658 in zip(*grid)]
        return sum((min(v1_833[v5_529], v3_818[v6_325]) - v7_559 for (v5_529, v2_765) in enumerate(grid) for (v6_325, v7_559) in enumerate(v2_765)))