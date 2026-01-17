class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        v1_754 = abs(x - z)
        v2_214 = abs(y - z)
        if v1_754  <  v2_214:
            return 1
        elif v1_754  >  v2_214:
            return 2
        else:
            return 0
