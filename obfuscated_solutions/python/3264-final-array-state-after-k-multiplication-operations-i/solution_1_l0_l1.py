class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int):
        v1_754 = len(nums)
        for v2_214 in range(k):
            v3_125 = 0
            for v4_859 in range(v1_754):
                if nums[v4_859] < nums[v3_125]:
                    v3_125 = v4_859
            nums[v3_125] *= multiplier
        return nums
