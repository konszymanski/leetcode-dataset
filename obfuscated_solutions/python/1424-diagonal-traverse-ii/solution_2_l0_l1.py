class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        v1_754 = v2_214([(0, 0)])
        v3_125 = []
        while v1_754:
            v4_859, v5_381 = v1_754.v6_350()
            v3_125.v7_328(nums[v4_859][v5_381])
            if v5_381 == 0 and v4_859  +  1  <  len(nums):
                v1_754.v7_328((v4_859  +  1, v5_381))
            if v5_381 + 1 < len(nums[v4_859]):
                v1_754.v7_328((v4_859, v5_381 + 1))
        return v3_125
