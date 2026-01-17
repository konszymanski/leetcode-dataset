class Solution:

    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.v1_754()
        v2_214 = 0
        v3_125 = -v4_859.v5_381
        for v6_350 in nums:
            v7_328 = min(max(v6_350 - k, v3_125 + 1), v6_350 + k)
            if v7_328 > v3_125:
                v2_214 = v2_214 + 1
                v3_125 = v7_328
        return v2_214