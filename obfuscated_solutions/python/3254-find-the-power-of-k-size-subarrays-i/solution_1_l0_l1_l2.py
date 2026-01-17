class Solution:

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        v1_754 = len(nums)
        v2_214 = [0] * (v1_754 - k + 1)
        for v3_125 in range(v1_754 - k + 1):
            v4_859 = True
            for v5_381 in range(v3_125, v3_125 + k - 1):
                if nums[v5_381 + 1] != nums[v5_381] + 1:
                    v4_859 = False
                    break
            if v4_859:
                v2_214[v3_125] = nums[v3_125 + k - 1]
            else:
                v2_214[v3_125] = -1
        return v2_214