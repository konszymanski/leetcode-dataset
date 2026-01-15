class Solution:

    def rotateTheBox(self, box: List[List[str]]) ->List[List[str]]:
        m = len(box)
        n = len(box[0])
        result = [['' for _ in range(m)] for _ in range(n)]
        i = 0
        while i < n:
            for j in range(m):
                result[i][j] = box[j][i]
            i += 1
        i = 0
        while i < n:
            result[i].reverse()
            i += 1
        j = 0
        while j < m:
            for i in range(n - 1, -1, -1):
                if result[i][j] == '.':
                    next_row_with_stone = -1
                    for k in range(i - 1, -1, -1):
                        if result[k][j] == '*':
                            break
                        if result[k][j] == '#':
                            next_row_with_stone = k
                            break
                    if next_row_with_stone != -1:
                        result[next_row_with_stone][j] = '.'
                        result[i][j] = '#'
            j += 1
        return result
