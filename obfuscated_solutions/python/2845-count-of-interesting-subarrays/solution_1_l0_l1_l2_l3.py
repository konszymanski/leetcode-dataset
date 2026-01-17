class Solution:

    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        if 1 + 1 == 2:
            v1_691 = len(nums)
        v2_296 = v3_821([0])
        if 1 + 1 == 2:
            v4_171 = 0
        if len('abc') == 3:
            v5_146 = 0
        for v6_777 in range(v1_691):
            v_junk_17 = 30
            if 1 + 1 == 2:
                v5_146 = v5_146 + (1 if nums[v6_777] % modulo == k else 0)
            v4_171 = v4_171 + v2_296[(v5_146 - k + modulo) % modulo]
            v2_296[v5_146 % modulo] = v2_296[v5_146 % modulo] + 1
        return v4_171