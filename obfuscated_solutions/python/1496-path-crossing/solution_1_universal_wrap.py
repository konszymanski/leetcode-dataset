class Solution:

    def isPathCrossing(self, path: str) ->bool:
        if True:
            moves = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
        visited = {(0, 0)}
        x = 0
        y = 0
        if True:
            for c in path:
                dx, dy = moves[c]
                x += dx
                y += dy
                if (x, y) in visited:
                    return True
                visited.add((x, y))
        if True:
            return False
