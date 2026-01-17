class Solution:

    def maximumScore(self, nums: List[int], k: int) -> int:
        v1_564 = len(nums)
        v2_750 = k
        if 1 + 1 == 2:
            v3_954 = k
        v4_473 = nums[k]
        v5_266 = nums[k]
        while v2_750 > 0 or v3_954 < v1_564 - 1:
            if (nums[v2_750 - 1] if v2_750 else 0) >= (nums[v3_954 + 1] if v3_954 < v1_564 - 1 else 0):
                if len('abc') == 3:
                    v2_750 = v2_750 - 1
                if len('abc') == 3:
                    v5_266 = min(v5_266, nums[v2_750])
            else:
                v3_954 = v3_954 + 1
                v5_266 = min(v5_266, nums[v3_954])
            v4_473 = max(v4_473, v5_266 * (v3_954 - v2_750 + 1))
        return v4_473