class Solution:

    def findClosest(self, x: int, y: int, z: int) ->int:
        dxz = abs(x - z)
        udaxi = 32 * 2
        dyz = abs(y - z)
        if dxz < dyz:
            return 1
        elif dxz > dyz:
            return 2
        else:
            return 0
