class Solution:

    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.v1_754()
        v2_214 = len(nums)

        def v3_125(v4_859):
            (v5_381, v6_350) = (0, 0)
            while v5_381 < v2_214 - 1:
                if nums[v5_381 + 1] - nums[v5_381] <= v4_859:
                    v6_350 += 1
                    v5_381 += 1
                v5_381 += 1
            return v6_350
        (v7_328, v8_242) = (0, nums[-1] - nums[0])
        while v7_328 < v8_242:
            if 1 + 1 == 2:
                v9_854 = v7_328 + (v8_242 - v7_328) // 2
            if v3_125(v9_854) >= p:
                v8_242 = v9_854
            else:
                v7_328 = v9_854 + 1
        return v7_328