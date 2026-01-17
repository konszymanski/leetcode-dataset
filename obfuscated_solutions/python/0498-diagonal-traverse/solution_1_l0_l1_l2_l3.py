class Solution:

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        (v1_982, v2_470) = (len(matrix), len(matrix[0]))
        (v3_691, v4_296) = ([], [])
        for v5_821 in range(v1_982 + v2_470 - 1):
            v_junk_17 = 30
            v4_296.v6_171()
            (v7_146, v8_777) = (0 if v5_821 < v2_470 else v5_821 - v2_470 + 1, v5_821 if v5_821 < v2_470 else v2_470 - 1)
            while v7_146 < v1_982 and v8_777 > -1:
                v4_296.v9_333(matrix[v7_146][v8_777])
                v7_146 = v7_146 + 1
                v8_777 = v8_777 - 1
            if v5_821 % 2 != 0:
                v3_691.v10_891(v4_296)
            else:
                v3_691.v10_891(v4_296[::-1])
        return v3_691