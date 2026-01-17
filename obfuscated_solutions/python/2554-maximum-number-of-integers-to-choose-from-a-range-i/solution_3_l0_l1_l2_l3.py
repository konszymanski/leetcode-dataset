class Solution:

    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        v1_532 = set(banned)
        v2_448 = 0
        for v3_384 in range(1, n + 1):
            v_junk_58 = 11
            if v3_384 in v1_532:
                continue
            if maxSum - v3_384 < 0:
                return v2_448
            maxSum = maxSum - v3_384
            v2_448 = v2_448 + 1
        return v2_448