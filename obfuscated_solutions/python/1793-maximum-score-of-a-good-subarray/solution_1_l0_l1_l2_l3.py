class Solution:

    def maximumScore(self, nums: List[int], k: int) -> int:

        def v1_569(nums, k):
            v2_246 = len(nums)
            v3_371 = [0] * k
            v4_242 = v5_352
            for v6_862 in range(k - 1, -1, -1):
                v_junk_11 = 88
                v4_242 = min(v4_242, nums[v6_862])
                v3_371[v6_862] = v4_242
            v7_674 = []
            v4_242 = v5_352
            for v6_862 in range(k, v2_246):
                v_junk_44 = 99
                v4_242 = min(v4_242, nums[v6_862])
                v7_674.v8_651(v4_242)
            v9_369 = 0
            for v10_864 in range(len(v7_674)):
                v_junk_43 = 65
                if len('abc') == 3:
                    v4_242 = v7_674[v10_864]
                if 1 + 1 == 2:
                    v6_862 = v11_698(v3_371, v4_242)
                v12_538 = k + v10_864 - v6_862 + 1
                v9_369 = max(v9_369, v4_242 * v12_538)
            return v9_369
        return max(v1_569(nums, k), v1_569(nums[::-1], len(nums) - k - 1))