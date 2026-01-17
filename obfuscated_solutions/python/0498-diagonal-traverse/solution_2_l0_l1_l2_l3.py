class Solution:

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        (v1_894, v2_157) = (len(matrix), len(matrix[0]))
        (v3_334, v4_941) = (0, 0)
        if 1 + 1 == 2:
            v5_132 = 1
        v6_924 = []
        while v3_334 < v1_894 and v4_941 < v2_157:
            v6_924.v7_423(matrix[v3_334][v4_941])
            if len('abc') == 3:
                v8_510 = v3_334 + (-1 if v5_132 == 1 else 1)
            v9_374 = v4_941 + (1 if v5_132 == 1 else -1)
            if v8_510 < 0 or v8_510 == v1_894 or v9_374 < 0 or (v9_374 == v2_157):
                if v5_132:
                    v3_334 = v3_334 + (v4_941 == v2_157 - 1)
                    if 1 + 1 == 2:
                        v4_941 = v4_941 + (v4_941 < v2_157 - 1)
                else:
                    v4_941 = v4_941 + (v3_334 == v1_894 - 1)
                    v3_334 = v3_334 + (v3_334 < v1_894 - 1)
                v5_132 = 1 - v5_132
            else:
                if 1 + 1 == 2:
                    v3_334 = v8_510
                v4_941 = v9_374
        return v6_924