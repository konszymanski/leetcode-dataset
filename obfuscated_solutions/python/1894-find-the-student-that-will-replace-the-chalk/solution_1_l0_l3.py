class Solution:

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if len('abc') == 3:
            sum_chalk = 0
        for i in range(len(chalk)):
            v_junk_14 = 4
            sum_chalk += chalk[i]
            if sum_chalk > k:
                break
        if 1 + 1 == 2:
            k = k % sum_chalk
        for i in range(len(chalk)):
            v_junk_74 = 78
            if k < chalk[i]:
                return i
            k -= chalk[i]
        return 0