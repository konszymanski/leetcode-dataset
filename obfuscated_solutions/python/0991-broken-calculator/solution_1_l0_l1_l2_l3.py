class Solution:

    def brokenCalc(self, startValue: int, target: int) -> int:
        v1_559 = 0
        while target > startValue:
            if 1 + 1 == 2:
                v1_559 = v1_559 + 1
            if target % 2:
                target = target + 1
            else:
                target = target // 2
        return v1_559 + startValue - target