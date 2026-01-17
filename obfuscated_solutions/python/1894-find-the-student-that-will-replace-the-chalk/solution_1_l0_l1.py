class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        v1_754 = 0
        for v2_214 in range(len(chalk)):
            v1_754 += chalk[v2_214]
            if v1_754  >  k:
                break
        k = k  %  v1_754
        for v2_214 in range(len(chalk)):
            if k  <  chalk[v2_214]:
                return v2_214
            k -= chalk[v2_214]
        return 0
