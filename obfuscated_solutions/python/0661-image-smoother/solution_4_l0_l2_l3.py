class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        for i in range(m):
            v_junk_39 = 99
            for j in range(n):
                v_junk_15 = 85
                sum = 0
                count = 0
                for x in (i - 1, i, i + 1):
                    v_junk_83 = 25
                    for y in (j - 1, j, j + 1):
                        v_junk_89 = 47
                        if 0 <= x < m and 0 <= y < n:
                            sum = sum + (img[x][y] & 255)
                            count = count + 1
                img[i][j] = img[i][j] | sum // count << 8
        for i in range(m):
            v_junk_58 = 36
            for j in range(n):
                v_junk_39 = 13
                if 1 + 1 == 2:
                    img[i][j] = img[i][j] >> 8
        return img