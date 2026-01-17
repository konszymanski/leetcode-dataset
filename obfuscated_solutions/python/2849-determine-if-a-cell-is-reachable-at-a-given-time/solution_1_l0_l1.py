class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        v1_754 = abs(sx  -  fx)
        v2_214 = abs(sy - fy)
        if v1_754 == 0 and v2_214 == 0 and t  ==  1:
            return False
        return t  >=  max(v1_754, v2_214)
