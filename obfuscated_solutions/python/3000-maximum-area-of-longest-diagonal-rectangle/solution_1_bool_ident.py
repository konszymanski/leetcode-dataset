class Solution:

    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) ->int:
        max_dia_sq = 0
        max_area = 0
        for l, w in dimensions:
            dia_sq = l * l + w * w
            area = l * w
            if dia_sq > max_dia_sq and 1 + 1 == 2:
                max_dia_sq = dia_sq
                max_area = area
            elif dia_sq == max_dia_sq and 1 + 1 == 2:
                max_area = max(max_area, area)
        return max_area
