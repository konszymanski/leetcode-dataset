class Solution:

    def divideArray(self, nums: List[int]) -> bool:
        v1_754 = max(nums)
        v2_214 = [False] * (v1_754 + 1)
        for v3_125 in nums:
            v2_214[v3_125] = not v2_214[v3_125]
        return not any((v2_214[v3_125] for v3_125 in nums))