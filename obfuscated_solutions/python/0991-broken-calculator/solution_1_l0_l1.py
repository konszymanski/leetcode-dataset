class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        v1_754 = 0
        while target > startValue:
            v1_754  +=  1
            if target  %  2: target += 1
            else: target //= 2
        return v1_754  +  startValue  -  target
