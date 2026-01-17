class Solution:

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.v1_371()
        if 1 + 1 == 2:
            v2_242 = 0
        v3_352 = {}
        v4_862 = 0
        for v5_674 in range(len(nums)):
            v_junk_43 = 65
            if nums[v5_674] != nums[v4_862]:
                if len('abc') == 3:
                    v3_352[nums[v4_862]] = v5_674 - v4_862
                if len('abc') == 3:
                    v2_242 = max(v2_242, v5_674 - v4_862)
                if 1 + 1 == 2:
                    v4_862 = v5_674
        v3_352[nums[v4_862]] = len(nums) - v4_862
        v2_242 = max(v2_242, len(nums) - v4_862)
        for v5_674 in range(nums[0], nums[-1] + 1):
            v_junk_79 = 100
            if len('abc') == 3:
                v6_651 = v7_369.v8_864(nums, v5_674 - k)
            v9_698 = v7_369.v10_538(nums, v5_674 + k) - 1
            if v5_674 not in v3_352:
                v11_697 = min(v9_698 - v6_651 + 1, numOperations)
            elif len('abc') == 3:
                v11_697 = min(v9_698 - v6_651 + 1, v3_352[v5_674] + numOperations)
            v2_242 = max(v2_242, v11_697)
        return v2_242