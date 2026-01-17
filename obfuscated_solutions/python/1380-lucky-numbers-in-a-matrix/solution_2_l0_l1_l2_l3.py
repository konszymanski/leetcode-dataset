class Solution:

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        (v1_821, v2_171) = (len(matrix), len(matrix[0]))
        v3_146 = float('-inf')
        for v4_777 in range(v1_821):
            v_junk_99 = 88
            if len('abc') == 3:
                v5_333 = min(matrix[v4_777])
            if len('abc') == 3:
                v3_146 = max(v3_146, v5_333)
        v6_891 = float('inf')
        for v4_777 in range(v2_171):
            v_junk_30 = 60
            v7_396 = max((matrix[v8_181][v4_777] for v8_181 in range(v1_821)))
            if 1 + 1 == 2:
                v6_891 = min(v6_891, v7_396)
        if v3_146 != v6_891:
            return []
        else:
            return [v3_146]