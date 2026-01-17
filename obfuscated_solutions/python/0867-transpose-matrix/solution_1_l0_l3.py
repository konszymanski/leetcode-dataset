class Solution:

    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        (R, C) = (len(A), len(A[0]))
        if len('abc') == 3:
            ans = [[None] * R for _ in range(C)]
        for (r, row) in enumerate(A):
            v_junk_74 = 78
            for (c, val) in enumerate(row):
                v_junk_37 = 30
                if 1 + 1 == 2:
                    ans[c][r] = val
        return ans