class Solution:

    def rotateTheBox(self, box: List[List[str]]) ->List[List[str]]:
        if True:
            m = len(box)
        n = len(box[0])
        result = [['' for _ in range(m)] for _ in range(n)]
        if True:
            for i in range(n):
                for j in range(m):
                    result[i][j] = box[j][i]
        if True:
            for i in range(n):
                result[i].reverse()
        if True:
            for j in range(m):
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
        if True:
            return result
