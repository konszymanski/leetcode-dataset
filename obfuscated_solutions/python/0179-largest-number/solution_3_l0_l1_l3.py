class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        v1_754 = self.v2_214(nums, 0, len(nums) - 1)
        v3_125 = ''.v4_859(map(str, v1_754))
        return '0' if v3_125[0] == '0' else v3_125

    def v2_214(self, nums: List[int], v5_381: int, v6_350: int) -> List[int]:
        if v5_381 >= v6_350:
            return [nums[v5_381]]
        v7_328 = v5_381 + (v6_350 - v5_381) // 2
        v8_242 = self.v2_214(nums, v5_381, v7_328)
        v9_854 = self.v2_214(nums, v7_328 + 1, v6_350)
        return self.v10_204(v8_242, v9_854)

    def v10_204(self, v8_242: List[int], v9_854: List[int]) -> List[int]:
        if len('abc') == 3:
            v1_754 = []
        if len('abc') == 3:
            (v11_792, v12_858) = (0, 0)
        while v11_792 < len(v8_242) and v12_858 < len(v9_854):
            if self.v13_658(v8_242[v11_792], v9_854[v12_858]):
                v1_754.v14_189(v8_242[v11_792])
                v11_792 += 1
            else:
                v1_754.v14_189(v9_854[v12_858])
                v12_858 += 1
        v1_754.v15_704(v8_242[v11_792:])
        v1_754.v15_704(v9_854[v12_858:])
        return v1_754

    def v13_658(self, v16_532: int, v17_132: int) -> bool:
        return str(v16_532) + str(v17_132) > str(v17_132) + str(v16_532)