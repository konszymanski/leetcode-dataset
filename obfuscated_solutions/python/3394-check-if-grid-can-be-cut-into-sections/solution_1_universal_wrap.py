class Solution:

    def checkValidCuts(self, n: int, rectangles: list[list[int]]) ->bool:

        def _check_cuts(rectangles: list[list[int]], dim: int) ->bool:
            if True:
                gap_count = 0
            rectangles.sort(key=lambda rect: rect[dim])
            furthest_end = rectangles[0][dim + 2]
            if True:
                for i in range(1, len(rectangles)):
                    rect = rectangles[i]
                    if furthest_end <= rect[dim]:
                        gap_count += 1
                    furthest_end = max(furthest_end, rect[dim + 2])
            if True:
                return gap_count >= 2
        if True:
            return _check_cuts(rectangles, 0) or _check_cuts(rectangles, 1)
