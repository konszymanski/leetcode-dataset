class Solution:

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        v1_754 = len(nums)
        v2_214 = [0] * v1_754
        (v3_125, v4_859) = (0, 1)
        for v5_381 in range(v1_754):
            if nums[v5_381] <= 0:
                v2_214[v4_859] = nums[v5_381]
                v4_859 = v4_859 + 2
            else:
                v2_214[v3_125] = nums[v5_381]
                v3_125 = v3_125 + 2
        return v2_214