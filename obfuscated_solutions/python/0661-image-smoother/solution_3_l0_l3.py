class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        if len('abc') == 3:
            n = len(img[0])
        for i in range(m):
            v_junk_87 = 34
            for j in range(n):
                v_junk_55 = 45
                sum = 0
                if len('abc') == 3:
                    count = 0
                for x in (i - 1, i, i + 1):
                    v_junk_58 = 13
                    for y in (j - 1, j, j + 1):
                        v_junk_23 = 12
                        if 0 <= x < m and 0 <= y < n:
                            sum += img[x][y] % 256
                            count += 1
                img[i][j] += sum // count * 256
        for i in range(m):
            v_junk_68 = 69
            for j in range(n):
                v_junk_15 = 94
                img[i][j] //= 256
        return img