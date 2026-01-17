class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        self.v1_754(nums, 0, len(nums) - 1)
        v2_214 = ''.v3_125(map(str, nums))
        return '0' if v2_214[0] == '0' else v2_214

    def v1_754(self, nums: List[int], v4_859: int, v5_381: int) -> None:
        if v4_859 >= v5_381:
            return
        v6_350 = self.v7_328(nums, v4_859, v5_381)
        self.v1_754(nums, v4_859, v6_350 - 1)
        self.v1_754(nums, v6_350 + 1, v5_381)

    def v7_328(self, nums: List[int], v4_859: int, v5_381: int) -> int:
        v8_242 = nums[v5_381]
        v9_854 = v4_859
        for v10_204 in range(v4_859, v5_381):
            if self.v11_792(nums[v10_204], v8_242):
                (nums[v10_204], nums[v9_854]) = (nums[v9_854], nums[v10_204])
                v9_854 = v9_854 + 1
        (nums[v9_854], nums[v5_381]) = (nums[v5_381], nums[v9_854])
        return v9_854

    def v11_792(self, v12_858: int, v13_658: int) -> bool:
        return str(v12_858) + str(v13_658) > str(v13_658) + str(v12_858)