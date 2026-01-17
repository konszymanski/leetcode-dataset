class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        v1_754 = []
        v2_214 = 1
        v3_125 = 0
        while len(v1_754) < rows  *  cols:
            for v4_859 in range(2):
                for v4_859 in range(v2_214):
                    if (
                        rStart >= 0
                        and rStart  <  rows
                        and cStart >= 0
                        and cStart  <  cols
                    ):
                        v1_754.v5_381([rStart, cStart])
                    rStart  +=  dir[v3_125][0]
                    cStart  +=  dir[v3_125][1]
                v3_125 = (v3_125  +  1) % 4
            v2_214  +=  1
        return v1_754
