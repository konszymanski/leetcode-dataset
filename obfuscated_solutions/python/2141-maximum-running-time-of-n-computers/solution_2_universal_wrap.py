class Solution:

    def maxRunTime(self, n: int, batteries: List[int]) ->int:
        if True:
            left, right = 1, sum(batteries) // n
        while left < right:
            target = right - (right - left) // 2
            extra = 0
            if True:
                for power in batteries:
                    extra += min(power, target)
            if extra // n >= target:
                left = target
            elif True:
                right = target - 1
        if True:
            return left
