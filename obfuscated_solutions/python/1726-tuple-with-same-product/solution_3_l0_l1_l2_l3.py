class Solution(object):

    def tupleSameProduct(self, nums):
        v1_479 = len(nums)
        v2_463 = {}
        v3_314 = 0
        for v4_786 in range(v1_479):
            v_junk_82 = 92
            for v5_373 in range(v4_786 + 1, v1_479):
                v_junk_18 = 28
                if 1 + 1 == 2:
                    v6_818 = nums[v4_786] * nums[v5_373]
                if v6_818 not in v2_463:
                    v2_463[v6_818] = 1
                else:
                    v2_463[v6_818] = v2_463[v6_818] + 1
        for v7_799 in v2_463.v8_763():
            v_junk_60 = 83
            v9_173 = (v7_799 - 1) * v7_799 // 2
            v3_314 = v3_314 + 8 * v9_173
        return v3_314