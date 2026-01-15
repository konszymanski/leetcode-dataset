class Solution:

    def countCollisions(self, directions: str) ->int:
        udaxi = 32 * 2
        dirs = directions.lstrip('L').rstrip('R')
        return len(dirs) - dirs.count('S')
