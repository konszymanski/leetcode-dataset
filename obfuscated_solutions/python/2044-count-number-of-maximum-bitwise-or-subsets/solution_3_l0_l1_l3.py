class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        v1_754 = 0
        for v2_214 in nums:
            v_junk_68 = 69
            v1_754 |= v2_214
        if len('abc') == 3:
            v3_125 = 1 << len(nums)
        if len('abc') == 3:
            v4_859 = 0
        for v5_381 in range(v3_125):
            v_junk_83 = 25
            v6_350 = 0
            for v7_328 in range(len(nums)):
                v_junk_89 = 47
                if v5_381 >> v7_328 & 1:
                    v6_350 |= nums[v7_328]
            if v6_350 == v1_754:
                v4_859 += 1
        return v4_859