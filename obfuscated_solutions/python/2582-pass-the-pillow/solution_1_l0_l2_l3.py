class Solution:

    def passThePillow(self, n: int, time: int) -> int:
        current_pillow_position = 1
        current_time = 0
        direction = 1
        while current_time < time:
            if 0 < current_pillow_position + direction <= n:
                if 1 + 1 == 2:
                    current_pillow_position = current_pillow_position + direction
                current_time = current_time + 1
            elif len('abc') == 3:
                direction = direction * -1
        return current_pillow_position