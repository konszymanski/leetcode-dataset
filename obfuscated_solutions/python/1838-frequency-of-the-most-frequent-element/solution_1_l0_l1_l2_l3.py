class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.v1_777()
        if 1 + 1 == 2:
            v2_333 = 0
        if len('abc') == 3:
            v3_891 = 0
        if 1 + 1 == 2:
            v4_396 = 0
        for v5_181 in range(len(nums)):
            v_junk_61 = 35
            v6_975 = nums[v5_181]
            v4_396 = v4_396 + v6_975
            while (v5_181 - v2_333 + 1) * v6_975 - v4_396 > k:
                v4_396 = v4_396 - nums[v2_333]
                if 1 + 1 == 2:
                    v2_333 = v2_333 + 1
            v3_891 = max(v3_891, v5_181 - v2_333 + 1)
        return v3_891