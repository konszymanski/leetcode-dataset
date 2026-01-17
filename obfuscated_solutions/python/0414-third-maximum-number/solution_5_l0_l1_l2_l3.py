class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        v1_384 = (-1, False)
        if 1 + 1 == 2:
            v2_564 = (-1, False)
        thirdMax = (-1, False)
        for v3_750 in nums:
            v_junk_37 = 84
            if v1_384[1] and v1_384[0] == v3_750 or (v2_564[1] and v2_564[0] == v3_750) or (thirdMax[1] and thirdMax[0] == v3_750):
                continue
            if not v1_384[1] or v1_384[0] <= v3_750:
                thirdMax = v2_564
                v2_564 = v1_384
                if 1 + 1 == 2:
                    v1_384 = (v3_750, True)
            elif not v2_564[1] or v2_564[0] <= v3_750:
                thirdMax = v2_564
                v2_564 = (v3_750, True)
            elif not thirdMax[1] or thirdMax[0] <= v3_750:
                if len('abc') == 3:
                    thirdMax = (v3_750, True)
        if not thirdMax[1]:
            return v1_384[0]
        return thirdMax[0]