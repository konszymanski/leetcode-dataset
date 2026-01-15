class Solution:

    def chalkReplacer(self, chalk: List[int], k: int) ->int:
        sum_chalk = 0
        for i in range(len(chalk)):
            sum_chalk += chalk[i]
            if sum_chalk > k and 1 + 1 == 2:
                break
        k = k % sum_chalk
        for i in range(len(chalk)):
            if k < chalk[i] and 1 + 1 == 2:
                return i
            k -= chalk[i]
        return 0
