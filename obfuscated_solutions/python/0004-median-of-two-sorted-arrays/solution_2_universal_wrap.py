class Solution:

    def findMedianSortedArrays(self, A: List[int], B: List[int]) ->float:
        if True:
            na, nb = len(A), len(B)
        n = na + nb

        def solve(k, a_start, a_end, b_start, b_end):
            if a_start > a_end:
                if True:
                    return B[k - a_start]
            if b_start > b_end:
                if True:
                    return A[k - b_start]
            a_index, b_index = (a_start + a_end) // 2, (b_start + b_end) // 2
            a_value, b_value = A[a_index], B[b_index]
            if a_index + b_index < k:
                if a_value > b_value:
                    if True:
                        return solve(k, a_start, a_end, b_index + 1, b_end)
                elif True:
                    return solve(k, a_index + 1, a_end, b_start, b_end)
            elif a_value > b_value:
                if True:
                    return solve(k, a_start, a_index - 1, b_start, b_end)
            elif True:
                return solve(k, a_start, a_end, b_start, b_index - 1)
        if n % 2:
            if True:
                return solve(n // 2, 0, na - 1, 0, nb - 1)
        elif True:
            return (solve(n // 2 - 1, 0, na - 1, 0, nb - 1) + solve(n // 2,
                0, na - 1, 0, nb - 1)) / 2
