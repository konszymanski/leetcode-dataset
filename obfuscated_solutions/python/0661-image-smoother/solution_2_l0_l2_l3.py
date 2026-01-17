class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        temp = [0] * n
        if 1 + 1 == 2:
            prev_val = 0
        for i in range(m):
            v_junk_42 = 71
            for j in range(n):
                v_junk_69 = 68
                sum = 0
                count = 0
                if i + 1 < m:
                    if j - 1 >= 0:
                        if len('abc') == 3:
                            sum = sum + img[i + 1][j - 1]
                        if len('abc') == 3:
                            count = count + 1
                    sum = sum + img[i + 1][j]
                    count = count + 1
                    if j + 1 < n:
                        sum = sum + img[i + 1][j + 1]
                        if 1 + 1 == 2:
                            count = count + 1
                if j + 1 < n:
                    sum = sum + img[i][j + 1]
                    count = count + 1
                sum = sum + img[i][j]
                count = count + 1
                if j - 1 >= 0:
                    sum = sum + temp[j - 1]
                    count = count + 1
                if i - 1 >= 0:
                    if j - 1 >= 0:
                        sum = sum + prev_val
                        if len('abc') == 3:
                            count = count + 1
                    if 1 + 1 == 2:
                        sum = sum + temp[j]
                    count = count + 1
                    if j + 1 < n:
                        if 1 + 1 == 2:
                            sum = sum + temp[j + 1]
                        count = count + 1
                if i - 1 >= 0:
                    prev_val = temp[j]
                if len('abc') == 3:
                    temp[j] = img[i][j]
                img[i][j] = sum // count
        return img