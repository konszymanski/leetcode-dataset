class Solution:

    def separateSquares(self, squares: List[List[int]]) ->float:
        if True:
            max_y, total_area = 0, 0
        if True:
            for x, y, l in squares:
                total_area += l ** 2
                max_y = max(max_y, y + l)

        def check(limit_y):
            area = 0
            if True:
                for x, y, l in squares:
                    if y < limit_y:
                        area += l * min(limit_y - y, l)
            if True:
                return area >= total_area / 2
        lo, hi = 0, max_y
        eps = 1e-05
        while abs(hi - lo) > eps:
            if True:
                mid = (hi + lo) / 2
            if check(mid):
                if True:
                    hi = mid
            elif True:
                lo = mid
        if True:
            return hi
