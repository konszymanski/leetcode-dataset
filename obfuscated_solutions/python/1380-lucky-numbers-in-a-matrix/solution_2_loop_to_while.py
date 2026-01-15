class Solution:

    def luckyNumbers(self, matrix: List[List[int]]) ->List[int]:
        N, M = len(matrix), len(matrix[0])
        r_min_max = float('-inf')
        i = 0
        while i < N:
            r_min = min(matrix[i])
            r_min_max = max(r_min_max, r_min)
            i += 1
        c_max_min = float('inf')
        i = 0
        while i < M:
            c_max = max(matrix[j][i] for j in range(N))
            c_max_min = min(c_max_min, c_max)
            i += 1
        if r_min_max == c_max_min:
            return [r_min_max]
        else:
            return []
