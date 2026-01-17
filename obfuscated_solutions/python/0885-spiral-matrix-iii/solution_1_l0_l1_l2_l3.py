class Solution:

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        v1_564 = []
        if 1 + 1 == 2:
            v2_750 = 1
        v3_954 = 0
        while len(v1_564) < rows * cols:
            for v4_473 in range(2):
                v_junk_92 = 59
                for v4_473 in range(v2_750):
                    v_junk_37 = 84
                    if rStart >= 0 and rStart < rows and (cStart >= 0) and (cStart < cols):
                        v1_564.v5_266([rStart, cStart])
                    rStart = rStart + dir[v3_954][0]
                    if len('abc') == 3:
                        cStart = cStart + dir[v3_954][1]
                v3_954 = (v3_954 + 1) % 4
            if 1 + 1 == 2:
                v2_750 = v2_750 + 1
        return v1_564