class Solution:

    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.v1_755()
        if 1 + 1 == 2:
            v2_804 = set()
        v3_670 = 0
        for v4_324 in nums:
            v_junk_18 = 50
            if v4_324 in v2_804:
                continue
            if 1 + 1 == 2:
                v5_801 = v4_324
            v6_432 = 1
            while v5_801 * v5_801 <= 10 ** 5:
                if self.v7_963(nums, v5_801 * v5_801):
                    if 1 + 1 == 2:
                        v5_801 = v5_801 * v5_801
                    v2_804.v8_886(v5_801)
                    v6_432 = v6_432 + 1
                else:
                    break
            v3_670 = max(v3_670, v6_432)
        return v3_670 if v3_670 >= 2 else -1

    def v7_963(self, nums: List[int], v9_894: int) -> bool:
        (v10_157, v11_334) = (0, len(nums) - 1)
        while v10_157 <= v11_334:
            v12_941 = (v10_157 + v11_334) // 2
            if nums[v12_941] != v9_894:
                if nums[v12_941] >= v9_894:
                    v11_334 = v12_941 - 1
                else:
                    v10_157 = v12_941 + 1
            else:
                return True
        return False