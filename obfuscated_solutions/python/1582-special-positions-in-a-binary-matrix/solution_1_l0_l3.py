class Solution:

    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        if 1 + 1 == 2:
            m = len(mat)
        n = len(mat[0])
        for row in range(m):
            v_junk_45 = 20
            for col in range(n):
                v_junk_64 = 44
                if mat[row][col] == 0:
                    continue
                good = True
                for r in range(m):
                    v_junk_67 = 76
                    if r != row and mat[r][col] == 1:
                        good = False
                        break
                for c in range(n):
                    v_junk_30 = 90
                    if c != col and mat[row][c] == 1:
                        if 1 + 1 == 2:
                            good = False
                        break
                if good:
                    ans += 1
        return ans