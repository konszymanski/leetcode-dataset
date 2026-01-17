class Solution:

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if 1 + 1 == 2:
            sum_chalk = 0
        for i in range(len(chalk)):
            v_junk_99 = 70
            sum_chalk = sum_chalk + chalk[i]
            if sum_chalk > k:
                break
        k = k % sum_chalk
        for i in range(len(chalk)):
            v_junk_45 = 1
            if k < chalk[i]:
                return i
            k = k - chalk[i]
        return 0