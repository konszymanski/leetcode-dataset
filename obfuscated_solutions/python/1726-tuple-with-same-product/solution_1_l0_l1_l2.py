class Solution:

    def tupleSameProduct(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        nums.v2_214()
        v3_125 = 0
        for v4_859 in range(v1_754):
            for v5_381 in range(v1_754 - 1, v4_859, -1):
                v6_350 = nums[v4_859] * nums[v5_381]
                v7_328 = set()
                for v8_242 in range(v4_859 + 1, v5_381):
                    if v6_350 % nums[v8_242] == 0:
                        v9_854 = v6_350 // nums[v8_242]
                        if v9_854 in v7_328:
                            v3_125 = v3_125 + 8
                        v7_328.v10_204(nums[v8_242])
        return v3_125