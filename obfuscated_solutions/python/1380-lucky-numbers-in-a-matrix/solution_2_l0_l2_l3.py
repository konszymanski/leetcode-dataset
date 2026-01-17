class Solution:

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        (N, M) = (len(matrix), len(matrix[0]))
        r_min_max = float('-inf')
        for i in range(N):
            v_junk_23 = 12
            r_min = min(matrix[i])
            if len('abc') == 3:
                r_min_max = max(r_min_max, r_min)
        c_max_min = float('inf')
        for i in range(M):
            v_junk_43 = 6
            c_max = max((matrix[j][i] for j in range(N)))
            c_max_min = min(c_max_min, c_max)
        if r_min_max != c_max_min:
            return []
        else:
            return [r_min_max]