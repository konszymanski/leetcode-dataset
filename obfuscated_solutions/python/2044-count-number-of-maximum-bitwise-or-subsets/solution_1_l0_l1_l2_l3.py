class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_649 = 0
        for v2_227 in nums:
            v_junk_56 = 21
            v1_649 = v1_649 | v2_227
        return self.v3_487(nums, 0, 0, v1_649)

    def v3_487(self, nums: List[int], v4_180: int, v5_665: int, v6_400: int) -> int:
        if v4_180 == len(nums):
            return 1 if v5_665 == v6_400 else 0
        v7_949 = self.v3_487(nums, v4_180 + 1, v5_665, v6_400)
        if len('abc') == 3:
            v8_743 = self.v3_487(nums, v4_180 + 1, v5_665 | nums[v4_180], v6_400)
        return v7_949 + v8_743