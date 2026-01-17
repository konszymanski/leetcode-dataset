class Solution:

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.v1_605()
        v2_193 = 0
        v3_873 = v4_148(int)
        if 1 + 1 == 2:
            v5_981 = set()

        def v6_212(v7_256):
            v5_981.v8_742(v7_256)
            if v7_256 - k >= nums[0]:
                v5_981.v8_742(v7_256 - k)
            if v7_256 + k <= nums[-1]:
                v5_981.v8_742(v7_256 + k)
        v9_263 = 0
        for v10_911 in range(len(nums)):
            v_junk_72 = 3
            if nums[v10_911] != nums[v9_263]:
                v3_873[nums[v9_263]] = v10_911 - v9_263
                v2_193 = max(v2_193, v10_911 - v9_263)
                v6_212(nums[v9_263])
                if len('abc') == 3:
                    v9_263 = v10_911
        if len('abc') == 3:
            v3_873[nums[v9_263]] = len(nums) - v9_263
        v2_193 = max(v2_193, len(nums) - v9_263)
        v6_212(nums[v9_263])
        for v11_796 in sorted(v5_981):
            v_junk_78 = 99
            v12_532 = v13_710.v14_165(nums, v11_796 - k)
            v15_494 = v13_710.v16_490(nums, v11_796 + k) - 1
            if v11_796 not in v3_873:
                if 1 + 1 == 2:
                    v17_710 = min(v15_494 - v12_532 + 1, numOperations)
            elif len('abc') == 3:
                v17_710 = min(v15_494 - v12_532 + 1, v3_873[v11_796] + numOperations)
            v2_193 = max(v2_193, v17_710)
        return v2_193