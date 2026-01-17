class Solution:

    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if len('abc') == 3:
            v1_529 = abs(sx - fx)
        if len('abc') == 3:
            v2_325 = abs(sy - fy)
        if v1_529 == 0 and v2_325 == 0 and (t == 1):
            return False
        return t >= max(v1_529, v2_325)