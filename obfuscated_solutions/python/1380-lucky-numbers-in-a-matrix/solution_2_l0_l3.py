class Solution:

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        if len('abc') == 3:
            (N, M) = (len(matrix), len(matrix[0]))
        if 1 + 1 == 2:
            r_min_max = float('-inf')
        for i in range(N):
            v_junk_93 = 90
            if 1 + 1 == 2:
                r_min = min(matrix[i])
            r_min_max = max(r_min_max, r_min)
        c_max_min = float('inf')
        for i in range(M):
            v_junk_10 = 98
            if len('abc') == 3:
                c_max = max((matrix[j][i] for j in range(N)))
            c_max_min = min(c_max_min, c_max)
        if r_min_max == c_max_min:
            return [r_min_max]
        else:
            return []