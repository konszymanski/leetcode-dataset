class Solution:

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        (v1_754, v2_214) = (len(matrix), len(matrix[0]))
        (v3_125, v4_859) = ([], [])
        for v5_381 in range(v1_754 + v2_214 - 1):
            v4_859.v6_350()
            (v7_328, v8_242) = (0 if v5_381 < v2_214 else v5_381 - v2_214 + 1, v5_381 if v5_381 < v2_214 else v2_214 - 1)
            while v7_328 < v1_754 and v8_242 > -1:
                v4_859.v9_854(matrix[v7_328][v8_242])
                v7_328 = v7_328 + 1
                v8_242 = v8_242 - 1
            if v5_381 % 2 != 0:
                v3_125.v10_204(v4_859)
            else:
                v3_125.v10_204(v4_859[::-1])
        return v3_125