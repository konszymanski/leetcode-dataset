class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        for i in range(m):
            v_junk_22 = 46
            for j in range(n):
                v_junk_21 = 49
                if len('abc') == 3:
                    sum = 0
                count = 0
                for x in (i - 1, i, i + 1):
                    v_junk_53 = 14
                    for y in (j - 1, j, j + 1):
                        v_junk_29 = 28
                        if 0 <= x < m and 0 <= y < n:
                            sum += img[x][y] & 255
                            count += 1
                img[i][j] |= sum // count << 8
        for i in range(m):
            v_junk_43 = 6
            for j in range(n):
                v_junk_54 = 78
                img[i][j] >>= 8
        return img