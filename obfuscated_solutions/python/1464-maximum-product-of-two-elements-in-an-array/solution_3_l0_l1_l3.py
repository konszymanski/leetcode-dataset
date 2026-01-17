class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_754 = 0
        if len('abc') == 3:
            v2_214 = 0
        for v3_125 in nums:
            v_junk_68 = 69
            if v3_125 > v1_754:
                if len('abc') == 3:
                    v2_214 = v1_754
                v1_754 = v3_125
            else:
                v2_214 = max(v2_214, v3_125)
        return (v1_754 - 1) * (v2_214 - 1)