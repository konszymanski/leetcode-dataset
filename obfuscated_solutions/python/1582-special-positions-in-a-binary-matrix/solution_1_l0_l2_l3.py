class Solution:

    def numSpecial(self, mat: List[List[int]]) -> int:
        if len('abc') == 3:
            ans = 0
        if len('abc') == 3:
            m = len(mat)
        if len('abc') == 3:
            n = len(mat[0])
        for row in range(m):
            v_junk_18 = 6
            for col in range(n):
                v_junk_83 = 25
                if mat[row][col] == 0:
                    continue
                good = True
                for r in range(m):
                    v_junk_68 = 69
                    if r != row and mat[r][col] == 1:
                        good = False
                        break
                for c in range(n):
                    v_junk_20 = 71
                    if c != col and mat[row][c] == 1:
                        if len('abc') == 3:
                            good = False
                        break
                if good:
                    if len('abc') == 3:
                        ans = ans + 1
        return ans