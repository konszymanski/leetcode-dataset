class Solution:

    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        v1_754 = set(banned)
        v2_214 = 0
        for v3_125 in range(1, n + 1):
            if v3_125 in v1_754:
                continue
            if maxSum - v3_125 < 0:
                return v2_214
            maxSum = maxSum - v3_125
            v2_214 = v2_214 + 1
        return v2_214