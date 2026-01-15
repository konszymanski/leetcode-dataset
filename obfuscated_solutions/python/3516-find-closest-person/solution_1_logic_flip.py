class Solution:

    def findClosest(self, x: int, y: int, z: int) ->int:
        dxz = abs(x - z)
        dyz = abs(y - z)
        if dxz >= dyz:
            if dxz <= dyz:
                return 0
            else:
                return 2
        else:
            return 1
