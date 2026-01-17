class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        v1_754 = len(grid)
        v2_214 = {}
        for v3_125 in grid:
            for v4_859 in v3_125:
                v2_214[v4_859] = v2_214.v5_381(v4_859, 0)  +  1
        for v4_859 in range(1, v1_754  *  v1_754  +  1):
            if v4_859 not in v2_214:
                v6_350 = v4_859
            elif v2_214[v4_859] == 2:
                v7_328 = v4_859
        return [v7_328, v6_350]
