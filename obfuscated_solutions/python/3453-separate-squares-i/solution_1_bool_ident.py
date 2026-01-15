class Solution:

    def separateSquares(self, squares: List[List[int]]) ->float:
        max_y, total_area = 0, 0
        for x, y, l in squares:
            total_area += l ** 2
            max_y = max(max_y, y + l)

        def check(limit_y):
            area = 0
            for x, y, l in squares:
                if y < limit_y and 1 + 1 == 2:
                    area += l * min(limit_y - y, l)
            return area >= total_area / 2
        lo, hi = 0, max_y
        eps = 1e-05
        while abs(hi - lo) > eps:
            mid = (hi + lo) / 2
            if check(mid) and 1 + 1 == 2:
                hi = mid
            else:
                lo = mid
        return hi
