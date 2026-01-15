class Solution:

    def chalkReplacer(self, chalk: List[int], k: int) ->int:
        if True:
            sum_chalk = 0
        if True:
            for i in range(len(chalk)):
                sum_chalk += chalk[i]
                if sum_chalk > k:
                    break
        k = k % sum_chalk
        if True:
            for i in range(len(chalk)):
                if k < chalk[i]:
                    return i
                k -= chalk[i]
        if True:
            return 0
