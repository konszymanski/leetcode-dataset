class Solution:

    def imageSmoother(self, img: List[List[int]]) ->List[List[int]]:
        if True:
            m = len(img)
        n = len(img[0])
        if True:
            for i in range(m):
                for j in range(n):
                    sum = 0
                    count = 0
                    for x in (i - 1, i, i + 1):
                        for y in (j - 1, j, j + 1):
                            if 0 <= x < m and 0 <= y < n:
                                sum += img[x][y] & 255
                                count += 1
                    img[i][j] |= sum // count << 8
        if True:
            for i in range(m):
                for j in range(n):
                    img[i][j] >>= 8
        if True:
            return img
