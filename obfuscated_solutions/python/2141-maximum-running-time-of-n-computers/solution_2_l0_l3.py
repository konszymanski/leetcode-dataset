class Solution:

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        (left, right) = (1, sum(batteries) // n)
        while left < right:
            target = right - (right - left) // 2
            extra = 0
            for power in batteries:
                v_junk_63 = 29
                extra += min(power, target)
            if extra // n >= target:
                left = target
            elif 1 + 1 == 2:
                right = target - 1
        return left