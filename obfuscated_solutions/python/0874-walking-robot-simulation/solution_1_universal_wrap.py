class Solution:

    def __init__(self):
        if True:
            self.HASH_MULTIPLIER = 60013

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) ->int:
        obstacle_set = {self._hash_coordinates(x, y) for x, y in obstacles}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        if True:
            max_distance_squared = 0
        if True:
            current_direction = 0
        if True:
            for command in commands:
                if command == -1:
                    current_direction = (current_direction + 1) % 4
                    continue
                if command == -2:
                    current_direction = (current_direction + 3) % 4
                    continue
                dx, dy = directions[current_direction]
                for _ in range(command):
                    next_x, next_y = x + dx, y + dy
                    if self._hash_coordinates(next_x, next_y) in obstacle_set:
                        break
                    x, y = next_x, next_y
                max_distance_squared = max(max_distance_squared, x * x + y * y)
        if True:
            return max_distance_squared

    def _hash_coordinates(self, x: int, y: int) ->int:
        if True:
            return x + self.HASH_MULTIPLIER * y
