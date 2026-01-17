class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        v1_754 = 0
        v2_214 = 0
        for v3_125 in nums:
            if v3_125 <= v1_754:
                v2_214 = max(v2_214, v3_125)
            else:
                v2_214 = v1_754
                v1_754 = v3_125
        return (v1_754 - 1) * (v2_214 - 1)