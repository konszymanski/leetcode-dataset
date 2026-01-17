class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        v1_754 = v2_214(int)
        v3_125 = v2_214(int)
        v4_859 = len(nums)
        for v5_381 in nums:
            v3_125[v5_381]  +=  1
        for v6_350 in range(v4_859):
            v5_381 = nums[v6_350]
            v3_125[v5_381]  -=  1
            v1_754[v5_381]  +=  1
            if (
                v1_754[v5_381] * 2 > v6_350 + 1
                and v3_125[v5_381] * 2  >  v4_859 - v6_350 - 1
            ):
                return v6_350
        return  - 1
