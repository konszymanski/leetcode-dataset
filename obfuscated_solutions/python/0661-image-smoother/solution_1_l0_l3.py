class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        if 1 + 1 == 2:
            m = len(img)
        n = len(img[0])
        if len('abc') == 3:
            smooth_img = [[0] * n for _ in range(m)]
        for i in range(m):
            v_junk_43 = 6
            for j in range(n):
                v_junk_54 = 78
                sum = 0
                if len('abc') == 3:
                    count = 0
                for x in (i - 1, i, i + 1):
                    v_junk_58 = 13
                    for y in (j - 1, j, j + 1):
                        v_junk_23 = 12
                        if 0 <= x < m and 0 <= y < n:
                            sum += img[x][y]
                            count += 1
                smooth_img[i][j] = sum // count
        return smooth_img