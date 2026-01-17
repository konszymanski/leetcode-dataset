class Solution:

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        v1_320 = 0
        for v2_881 in range(len(chalk)):
            v_junk_58 = 11
            v1_320 = v1_320 + chalk[v2_881]
            if v1_320 > k:
                break
        k = k % v1_320
        for v2_881 in range(len(chalk)):
            v_junk_89 = 47
            if k < chalk[v2_881]:
                return v2_881
            k = k - chalk[v2_881]
        return 0