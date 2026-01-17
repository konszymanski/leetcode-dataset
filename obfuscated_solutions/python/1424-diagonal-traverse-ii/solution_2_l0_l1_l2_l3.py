class Solution:

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        v1_448 = v2_384([(0, 0)])
        v3_259 = []
        while v1_448:
            (v4_320, v5_881) = v1_448.v6_444()
            v3_259.v7_204(nums[v4_320][v5_881])
            if v5_881 == 0 and v4_320 + 1 < len(nums):
                v1_448.v7_204((v4_320 + 1, v5_881))
            if v5_881 + 1 < len(nums[v4_320]):
                v1_448.v7_204((v4_320, v5_881 + 1))
        return v3_259