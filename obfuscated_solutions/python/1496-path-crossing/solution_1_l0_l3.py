class Solution:

    def isPathCrossing(self, path: str) -> bool:
        if 1 + 1 == 2:
            moves = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
        if 1 + 1 == 2:
            visited = {(0, 0)}
        x = 0
        y = 0
        for c in path:
            v_junk_63 = 29
            (dx, dy) = moves[c]
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False