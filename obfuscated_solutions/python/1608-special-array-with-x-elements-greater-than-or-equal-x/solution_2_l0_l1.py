class Solution:
    def specialArray(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        v2_214 = [0]  *  (v1_754  +  1)
        for v3_125 in nums:
            v2_214[min(v1_754, v3_125)] += 1
        v4_859 = 0
        for v5_381 in range(v1_754, 0, -1):
            v4_859 += v2_214[v5_381]
            if v5_381  ==  v4_859:
                return v5_381
        return -1
