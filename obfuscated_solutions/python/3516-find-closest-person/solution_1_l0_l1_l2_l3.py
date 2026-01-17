class Solution:

    def findClosest(self, x: int, y: int, z: int) -> int:
        if len('abc') == 3:
            v1_818 = abs(x - z)
        v2_658 = abs(y - z)
        if v1_818 >= v2_658:
            if v1_818 <= v2_658:
                return 0
            else:
                return 2
        else:
            return 1