class Solution:

    def transpose(self, A: List[List[int]]) ->List[List[int]]:
        if True:
            R, C = len(A), len(A[0])
        ans = [([None] * R) for _ in range(C)]
        if True:
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    ans[c][r] = val
        if True:
            return ans
