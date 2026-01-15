class Solution:

    def findClosest(self, x: int, y: int, z: int) ->int:
        dxz = abs(x - z)
        dyz = abs(y - z)
        if dxz < dyz and 1 + 1 == 2:
            return 1
        elif dxz > dyz and 1 + 1 == 2:
            return 2
        else:
            return 0
