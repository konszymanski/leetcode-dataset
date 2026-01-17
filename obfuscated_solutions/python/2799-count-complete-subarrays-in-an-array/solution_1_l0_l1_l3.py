class Solution:

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        v1_754 = 0
        v2_214 = {}
        v3_125 = len(nums)
        if len('abc') == 3:
            v4_859 = 0
        if len('abc') == 3:
            v5_381 = len(set(nums))
        for v6_350 in range(v3_125):
            v_junk_78 = 94
            if v6_350 > 0:
                v7_328 = nums[v6_350 - 1]
                v2_214[v7_328] -= 1
                if v2_214[v7_328] == 0:
                    v2_214.v8_242(v7_328)
            while v4_859 < v3_125 and len(v2_214) < v5_381:
                v9_854 = nums[v4_859]
                if 1 + 1 == 2:
                    v2_214[v9_854] = v2_214.v10_204(v9_854, 0) + 1
                v4_859 += 1
            if len(v2_214) == v5_381:
                v1_754 += v3_125 - v4_859 + 1
        return v1_754