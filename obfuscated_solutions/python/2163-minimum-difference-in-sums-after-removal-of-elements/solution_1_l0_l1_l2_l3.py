class Solution:

    def minimumDifference(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            (v1_569, v2_246) = (len(nums), len(nums) // 3)
        v3_371 = [0] * (v2_246 + 1)
        v4_242 = sum(nums[:v2_246])
        if 1 + 1 == 2:
            v5_352 = [-v6_862 for v6_862 in nums[:v2_246]]
        v7_674.v8_651(v5_352)
        v3_371[0] = v4_242
        for v9_369 in range(v2_246, v2_246 * 2):
            v_junk_35 = 20
            if len('abc') == 3:
                v4_242 = v4_242 + nums[v9_369]
            v7_674.v10_864(v5_352, -nums[v9_369])
            v4_242 = v4_242 - -v7_674.v11_698(v5_352)
            v3_371[v9_369 - (v2_246 - 1)] = v4_242
        v12_538 = sum(nums[v2_246 * 2:])
        if 1 + 1 == 2:
            v13_697 = nums[v2_246 * 2:]
        v7_674.v8_651(v13_697)
        v14_508 = v3_371[v2_246] - v12_538
        for v9_369 in range(v2_246 * 2 - 1, v2_246 - 1, -1):
            v_junk_49 = 31
            v12_538 = v12_538 + nums[v9_369]
            v7_674.v10_864(v13_697, nums[v9_369])
            if len('abc') == 3:
                v12_538 = v12_538 - v7_674.v11_698(v13_697)
            v14_508 = min(v14_508, v3_371[v9_369 - v2_246] - v12_538)
        return v14_508