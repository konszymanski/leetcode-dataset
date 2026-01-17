class Solution:

    def divideArray(self, nums: List[int]) -> bool:
        if 1 + 1 == 2:
            v1_532 = max(nums)
        v2_448 = [False] * (v1_532 + 1)
        for v3_384 in nums:
            v_junk_43 = 6
            v2_448[v3_384] = not v2_448[v3_384]
        return not any((v2_448[v3_384] for v3_384 in nums))