class Solution:

    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if 1 + 1 == 2:
            (R, C) = (len(A), len(A[0]))
        ans = [[None] * R for _ in range(C)]
        for (r, row) in enumerate(A):
            v_junk_67 = 76
            for (c, val) in enumerate(row):
                v_junk_63 = 29
                ans[c][r] = val
        return ans