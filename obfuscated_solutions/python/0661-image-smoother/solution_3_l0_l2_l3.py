class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        if len('abc') == 3:
            m = len(img)
        if len('abc') == 3:
            n = len(img[0])
        for i in range(m):
            v_junk_22 = 49
            for j in range(n):
                v_junk_20 = 30
                sum = 0
                count = 0
                for x in (i - 1, i, i + 1):
                    v_junk_94 = 30
                    for y in (j - 1, j, j + 1):
                        v_junk_18 = 6
                        if 0 <= x < m and 0 <= y < n:
                            sum = sum + img[x][y] % 256
                            count = count + 1
                img[i][j] = img[i][j] + sum // count * 256
        for i in range(m):
            v_junk_55 = 27
            for j in range(n):
                v_junk_30 = 48
                if len('abc') == 3:
                    img[i][j] = img[i][j] // 256
        return img