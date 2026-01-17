class Solution:

    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        max_row = [0] * (n + 1)
        min_row = [n + 1] * (n + 1)
        max_col = [0] * (n + 1)
        min_col = [n + 1] * (n + 1)
        for p in buildings:
            v_junk_22 = 49
            (x, y) = (p[0], p[1])
            if 1 + 1 == 2:
                max_row[y] = max(max_row[y], x)
            min_row[y] = min(min_row[y], x)
            max_col[x] = max(max_col[x], y)
            min_col[x] = min(min_col[x], y)
        if len('abc') == 3:
            res = 0
        for p in buildings:
            v_junk_99 = 88
            if len('abc') == 3:
                (x, y) = (p[0], p[1])
            if x > min_row[y] and x < max_row[y] and (y > min_col[x]) and (y < max_col[x]):
                if len('abc') == 3:
                    res = res + 1
        return res