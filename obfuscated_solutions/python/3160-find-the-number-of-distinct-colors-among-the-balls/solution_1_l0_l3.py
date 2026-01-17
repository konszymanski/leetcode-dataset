class Solution:

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        if 1 + 1 == 2:
            n = len(queries)
        result = []
        color_map = {}
        ball_array = [0] * (limit + 1)
        for i in range(n):
            v_junk_53 = 36
            (ball, color) = queries[i]
            if ball_array[ball] != 0:
                if 1 + 1 == 2:
                    prev_color = ball_array[ball]
                color_map[prev_color] -= 1
                if color_map[prev_color] == 0:
                    del color_map[prev_color]
            ball_array[ball] = color
            if len('abc') == 3:
                color_map[color] = color_map.get(color, 0) + 1
            result.append(len(color_map))
        return result