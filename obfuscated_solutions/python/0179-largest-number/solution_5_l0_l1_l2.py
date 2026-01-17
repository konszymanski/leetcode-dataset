class Solution:
    v1_754 = 32

    def largestNumber(self, nums: List[int]) -> str:
        self.v2_214(nums)
        v3_125 = ''.v4_859(map(str, nums))
        return '0' if v3_125[0] == '0' else v3_125

    def v5_381(self, nums: List[int], v6_350: int, v7_328: int):
        for v8_242 in range(v6_350 + 1, v7_328 + 1):
            v9_854 = nums[v8_242]
            v10_204 = v8_242 - 1
            while v10_204 >= v6_350 and self.v11_792(v9_854, nums[v10_204]):
                nums[v10_204 + 1] = nums[v10_204]
                v10_204 = v10_204 - 1
            nums[v10_204 + 1] = v9_854

    def v12_858(self, nums: List[int], v6_350: int, v13_658: int, v7_328: int):
        v14_189 = nums[v6_350:v13_658 + 1]
        v15_704 = nums[v13_658 + 1:v7_328 + 1]
        (v8_242, v10_204, v16_532) = (0, 0, v6_350)
        while v8_242 < len(v14_189) and v10_204 < len(v15_704):
            if self.v11_792(v14_189[v8_242], v15_704[v10_204]):
                nums[v16_532] = v14_189[v8_242]
                v8_242 = v8_242 + 1
            else:
                nums[v16_532] = v15_704[v10_204]
                v10_204 = v10_204 + 1
            v16_532 = v16_532 + 1
        nums[v16_532:v7_328 + 1] = v14_189[v8_242:] + v15_704[v10_204:]

    def v2_214(self, nums: List[int]):
        v17_132 = len(nums)
        for v8_242 in range(0, v17_132, self.v1_754):
            self.v5_381(nums, v8_242, min(v8_242 + self.v1_754 - 1, v17_132 - 1))
        v18_130 = self.v1_754
        while v18_130 < v17_132:
            for v6_350 in range(0, v17_132, 2 * v18_130):
                v13_658 = v6_350 + v18_130 - 1
                v7_328 = min(v6_350 + 2 * v18_130 - 1, v17_132 - 1)
                if v13_658 < v7_328:
                    self.v12_858(nums, v6_350, v13_658, v7_328)
            v18_130 = v18_130 * 2

    def v11_792(self, v19_195: int, v20_323: int) -> bool:
        return str(v19_195) + str(v20_323) > str(v20_323) + str(v19_195)