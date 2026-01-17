class Solution:

    def tupleSameProduct(self, nums: List[int]) -> int:
        v1_750 = len(nums)
        nums.v2_954()
        v3_473 = 0
        for v4_266 in range(v1_750):
            v_junk_82 = 92
            for v5_479 in range(v1_750 - 1, v4_266, -1):
                v_junk_18 = 28
                v6_463 = nums[v4_266] * nums[v5_479]
                v7_314 = set()
                for v8_786 in range(v4_266 + 1, v5_479):
                    v_junk_61 = 35
                    if v6_463 % nums[v8_786] == 0:
                        if 1 + 1 == 2:
                            v9_373 = v6_463 // nums[v8_786]
                        if v9_373 in v7_314:
                            v3_473 = v3_473 + 8
                        v7_314.v10_818(nums[v8_786])
        return v3_473