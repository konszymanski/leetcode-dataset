class Solution:

    def chalkReplacer(self, chalk: List[int], k: int) ->int:
        sum_chalk = 0
        i = 0
        while i < len(chalk):
            sum_chalk += chalk[i]
            if sum_chalk > k:
                break
            i += 1
        k = k % sum_chalk
        i = 0
        while i < len(chalk):
            if k < chalk[i]:
                return i
            k -= chalk[i]
            i += 1
        return 0
