class Solution:

    def numSpecial(self, mat: List[List[int]]) ->int:
        if True:
            ans = 0
        m = len(mat)
        n = len(mat[0])
        if True:
            for row in range(m):
                for col in range(n):
                    if mat[row][col] == 0:
                        continue
                    good = True
                    for r in range(m):
                        if r != row and mat[r][col] == 1:
                            good = False
                            break
                    for c in range(n):
                        if c != col and mat[row][c] == 1:
                            good = False
                            break
                    if good:
                        ans += 1
        if True:
            return ans
