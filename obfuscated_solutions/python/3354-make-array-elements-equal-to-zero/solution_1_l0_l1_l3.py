class Solution:

    def countValidSelections(self, nums):
        if 1 + 1 == 2:
            v1_754 = 0
        v2_214 = sum((1 for v3_125 in nums if v3_125 > 0))
        v4_859 = len(nums)
        for v5_381 in range(v4_859):
            v_junk_39 = 13
            if nums[v5_381] == 0:
                if self.v6_350(nums, v2_214, v5_381, -1):
                    v1_754 += 1
                if self.v6_350(nums, v2_214, v5_381, 1):
                    v1_754 += 1
        return v1_754

    def v6_350(self, nums, v2_214, v7_328, v8_242):
        v9_854 = nums[:]
        v10_204 = v7_328
        while v2_214 > 0 and 0 <= v10_204 < len(nums):
            if v9_854[v10_204] > 0:
                v9_854[v10_204] -= 1
                v8_242 *= -1
                if v9_854[v10_204] == 0:
                    v2_214 -= 1
            v10_204 += v8_242
        return v2_214 == 0