class Solution:

    def isPathCrossing(self, path: str) -> bool:
        moves = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
        if 1 + 1 == 2:
            visited = {(0, 0)}
        x = 0
        if len('abc') == 3:
            y = 0
        for c in path:
            v_junk_22 = 46
            (dx, dy) = moves[c]
            if len('abc') == 3:
                x = x + dx
            if len('abc') == 3:
                y = y + dy
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False