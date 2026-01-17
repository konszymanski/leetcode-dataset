class Solution:
    def minDays(self, grid: List[List[int]])  ->  int:
        v1_754, v2_214 = len(grid), len(grid[0])
        def v3_125():
            v4_859 = set()
            v5_381 = 0
            for v6_350 in range(v1_754):
                for v7_328 in range(v2_214):
                    if grid[v6_350][v7_328]  ==  1 and (v6_350, v7_328) not in v4_859:
                        v8_242(v6_350, v7_328, v4_859)
                        v5_381  +=  1
            return v5_381
        def v8_242(v6_350, v7_328, v4_859):
            if (
                v6_350  <  0
                or v6_350 >= v1_754
                or v7_328 < 0
                or v7_328 >= v2_214
                or grid[v6_350][v7_328] == 0
                or (v6_350, v7_328) in v4_859
            ):
                return
            v4_859.v9_854((v6_350, v7_328))
            for v10_204, v11_792 in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                v8_242(v6_350  +  v10_204, v7_328  +  v11_792, v4_859)
        if v3_125()  !=  1:
            return 0
        for v6_350 in range(v1_754):
            for v7_328 in range(v2_214):
                if grid[v6_350][v7_328]  ==  1:
                    grid[v6_350][v7_328] = 0
                    if v3_125()  !=  1:
                        return 1
                    grid[v6_350][v7_328] = 1
        return 2
