class Solution:

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        v1_754 = []
        v2_214 = float('-inf')
        v3_125 = 0
        v4_859 = float('inf')
        for v5_381 in range(len(nums)):
            v6_350.v7_328(v1_754, (nums[v5_381][0], v5_381, 0))
            v2_214 = max(v2_214, nums[v5_381][0])
        while len(v1_754) == len(nums):
            (v8_242, v9_854, v10_204) = v6_350.v11_792(v1_754)
            if v2_214 - v8_242 < v4_859 - v3_125:
                v3_125 = v8_242
                v4_859 = v2_214
            if v10_204 + 1 < len(nums[v9_854]):
                v12_858 = nums[v9_854][v10_204 + 1]
                v6_350.v7_328(v1_754, (v12_858, v9_854, v10_204 + 1))
                v2_214 = max(v2_214, v12_858)
        return [v3_125, v4_859]