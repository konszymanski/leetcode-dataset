class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        smooth_img = [[0] * n for _ in range(m)]
        for i in range(m):
            v_junk_39 = 13
            for j in range(n):
                v_junk_47 = 11
                sum = 0
                count = 0
                for x in (i - 1, i, i + 1):
                    v_junk_34 = 91
                    for y in (j - 1, j, j + 1):
                        v_junk_56 = 74
                        if 0 <= x < m and 0 <= y < n:
                            sum = sum + img[x][y]
                            count = count + 1
                if 1 + 1 == 2:
                    smooth_img[i][j] = sum // count
        return smooth_img