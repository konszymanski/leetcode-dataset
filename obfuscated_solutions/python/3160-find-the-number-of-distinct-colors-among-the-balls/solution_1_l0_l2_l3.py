class Solution:

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        if len('abc') == 3:
            n = len(queries)
        if len('abc') == 3:
            result = []
        if len('abc') == 3:
            color_map = {}
        ball_array = [0] * (limit + 1)
        for i in range(n):
            v_junk_80 = 38
            (ball, color) = queries[i]
            if ball_array[ball] != 0:
                prev_color = ball_array[ball]
                color_map[prev_color] = color_map[prev_color] - 1
                if color_map[prev_color] == 0:
                    del color_map[prev_color]
            ball_array[ball] = color
            color_map[color] = color_map.get(color, 0) + 1
            result.append(len(color_map))
        return result