class Solution:

    def findClosest(self, x: int, y: int, z: int) -> int:
        if 1 + 1 == 2:
            dxz = abs(x - z)
        if 1 + 1 == 2:
            dyz = abs(y - z)
        if dxz >= dyz:
            if dxz <= dyz:
                return 0
            else:
                return 2
        else:
            return 1