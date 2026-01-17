class Solution:

    def findClosest(self, x: int, y: int, z: int) -> int:
        v1_754 = abs(x - z)
        v2_214 = abs(y - z)
        if v1_754 >= v2_214:
            if v1_754 <= v2_214:
                return 0
            else:
                return 2
        else:
            return 1