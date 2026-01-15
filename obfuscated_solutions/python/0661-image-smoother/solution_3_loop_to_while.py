class Solution:

    def imageSmoother(self, img: List[List[int]]) ->List[List[int]]:
        m = len(img)
        n = len(img[0])
        i = 0
        while i < m:
            for j in range(n):
                sum = 0
                count = 0
                for x in (i - 1, i, i + 1):
                    for y in (j - 1, j, j + 1):
                        if 0 <= x < m and 0 <= y < n:
                            sum += img[x][y] % 256
                            count += 1
                img[i][j] += sum // count * 256
            i += 1
        i = 0
        while i < m:
            for j in range(n):
                img[i][j] //= 256
            i += 1
        return img
