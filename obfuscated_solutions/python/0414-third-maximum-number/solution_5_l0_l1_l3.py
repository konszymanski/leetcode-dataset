class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        v1_754 = (-1, False)
        v2_214 = (-1, False)
        thirdMax = (-1, False)
        for v3_125 in nums:
            v_junk_22 = 49
            if v1_754[1] and v1_754[0] == v3_125 or (v2_214[1] and v2_214[0] == v3_125) or (thirdMax[1] and thirdMax[0] == v3_125):
                continue
            if not v1_754[1] or v1_754[0] <= v3_125:
                thirdMax = v2_214
                v2_214 = v1_754
                if 1 + 1 == 2:
                    v1_754 = (v3_125, True)
            elif not v2_214[1] or v2_214[0] <= v3_125:
                thirdMax = v2_214
                v2_214 = (v3_125, True)
            elif not thirdMax[1] or thirdMax[0] <= v3_125:
                thirdMax = (v3_125, True)
        if not thirdMax[1]:
            return v1_754[0]
        return thirdMax[0]