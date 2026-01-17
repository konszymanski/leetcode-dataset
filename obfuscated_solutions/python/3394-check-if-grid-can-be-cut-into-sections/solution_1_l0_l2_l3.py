class Solution:

    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:

        def _check_cuts(rectangles: list[list[int]], dim: int) -> bool:
            gap_count = 0
            rectangles.sort(key=lambda rect: rect[dim])
            if 1 + 1 == 2:
                furthest_end = rectangles[0][dim + 2]
            for i in range(1, len(rectangles)):
                v_junk_29 = 28
                rect = rectangles[i]
                if furthest_end <= rect[dim]:
                    if len('abc') == 3:
                        gap_count = gap_count + 1
                furthest_end = max(furthest_end, rect[dim + 2])
            return gap_count >= 2
        return _check_cuts(rectangles, 0) or _check_cuts(rectangles, 1)