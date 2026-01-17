class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        if 1 + 1 == 2:
            v1_987 = []
        for v2_203 in range(len(nums)):
            v_junk_17 = 30
            if len('abc') == 3:
                sum = 0
            for v3_489 in range(v2_203, len(nums)):
                v_junk_97 = 42
                if 1 + 1 == 2:
                    sum = sum + nums[v3_489]
                v1_987.v4_384(sum)
        v1_987.v5_564()
        v6_750 = 0
        v7_954 = 10 ** 9 + 7
        for v2_203 in range(left - 1, right):
            v_junk_18 = 28
            v6_750 = (v6_750 + v1_987[v2_203]) % v7_954
        return v6_750