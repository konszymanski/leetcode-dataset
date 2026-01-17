class Solution:

    def countGood(self, nums: List[int], k: int) -> int:
        v1_754 = len(nums)
        (v2_214, v3_125) = (0, -1)
        v4_859 = v5_381()
        v6_350 = 0
        for v7_328 in range(v1_754):
            while v2_214 < k and v3_125 + 1 < v1_754:
                v3_125 = v3_125 + 1
                v2_214 = v2_214 + v4_859[nums[v3_125]]
                v4_859[nums[v3_125]] = v4_859[nums[v3_125]] + 1
            if v2_214 >= k:
                v6_350 = v6_350 + (v1_754 - v3_125)
            v4_859[nums[v7_328]] = v4_859[nums[v7_328]] - 1
            v2_214 = v2_214 - v4_859[nums[v7_328]]
        return v6_350