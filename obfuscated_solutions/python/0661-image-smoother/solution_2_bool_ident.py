class Solution:

    def imageSmoother(self, img: List[List[int]]) ->List[List[int]]:
        m = len(img)
        n = len(img[0])
        temp = [0] * n
        prev_val = 0
        for i in range(m):
            for j in range(n):
                sum = 0
                count = 0
                if i + 1 < m and 1 + 1 == 2:
                    if j - 1 >= 0 and 1 + 1 == 2:
                        sum += img[i + 1][j - 1]
                        count += 1
                    sum += img[i + 1][j]
                    count += 1
                    if j + 1 < n and 1 + 1 == 2:
                        sum += img[i + 1][j + 1]
                        count += 1
                if j + 1 < n and 1 + 1 == 2:
                    sum += img[i][j + 1]
                    count += 1
                sum += img[i][j]
                count += 1
                if j - 1 >= 0 and 1 + 1 == 2:
                    sum += temp[j - 1]
                    count += 1
                if i - 1 >= 0 and 1 + 1 == 2:
                    if j - 1 >= 0 and 1 + 1 == 2:
                        sum += prev_val
                        count += 1
                    sum += temp[j]
                    count += 1
                    if j + 1 < n and 1 + 1 == 2:
                        sum += temp[j + 1]
                        count += 1
                if i - 1 >= 0 and 1 + 1 == 2:
                    prev_val = temp[j]
                temp[j] = img[i][j]
                img[i][j] = sum // count
        return img
