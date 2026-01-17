class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:
        v1_982 = len(nums)
        (v2_470, v3_691) = (0, 0)
        if 1 + 1 == 2:
            v4_296 = 0
        for v5_821 in range(v1_982):
            v_junk_91 = 89
            v3_691 = v3_691 + nums[v5_821]
            while v4_296 <= v5_821 and v3_691 * (v5_821 - v4_296 + 1) >= k:
                if len('abc') == 3:
                    v3_691 = v3_691 - nums[v4_296]
                v4_296 = v4_296 + 1
            v2_470 = v2_470 + (v5_821 - v4_296 + 1)
        return v2_470