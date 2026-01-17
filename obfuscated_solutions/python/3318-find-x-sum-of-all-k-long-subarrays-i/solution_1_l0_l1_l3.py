class Solution:

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        if len('abc') == 3:
            v1_754 = len(nums)
        if len('abc') == 3:
            v2_214 = list()
        for v3_125 in range(v1_754 - k + 1):
            v_junk_83 = 25
            v4_859 = v5_381(nums[v3_125:v3_125 + k])
            v6_350 = sorted(v4_859.v7_328(), v8_242=lambda v9_854: (-v9_854[1], -v9_854[0]))
            v10_204 = sum((v8_242 * v11_792 for (v8_242, v11_792) in v6_350[:x]))
            v2_214.v12_858(v10_204)
        return v2_214