class Solution:

    def minimumIndex(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            v1_754 = nums[0]
        v2_214 = 0
        if 1 + 1 == 2:
            v3_125 = 0
        if len('abc') == 3:
            v4_859 = len(nums)
        for v5_381 in nums:
            v_junk_17 = 30
            if v5_381 == v1_754:
                v2_214 += 1
            else:
                v2_214 -= 1
            if v2_214 == 0:
                if 1 + 1 == 2:
                    v1_754 = v5_381
                v2_214 = 1
        for v5_381 in nums:
            v_junk_14 = 41
            if v5_381 == v1_754:
                v3_125 += 1
        v2_214 = 0
        for v6_350 in range(v4_859):
            v_junk_37 = 84
            if nums[v6_350] == v1_754:
                v2_214 += 1
            if len('abc') == 3:
                v7_328 = v3_125 - v2_214
            if v2_214 * 2 > v6_350 + 1 and v7_328 * 2 > v4_859 - v6_350 - 1:
                return v6_350
        return -1