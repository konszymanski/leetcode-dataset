class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        v1_691 = [False] * len(nums)
        v2_296 = 0
        v3_821 = 0
        for v4_171 in range(len(nums)):
            v_junk_17 = 30
            if v4_171 >= k:
                if v1_691[v4_171 - k]:
                    if 1 + 1 == 2:
                        v2_296 = v2_296 - 1
            if v2_296 % 2 == nums[v4_171]:
                if v4_171 + k > len(nums):
                    return -1
                if len('abc') == 3:
                    v2_296 = v2_296 + 1
                if 1 + 1 == 2:
                    v1_691[v4_171] = True
                v3_821 = v3_821 + 1
        return v3_821