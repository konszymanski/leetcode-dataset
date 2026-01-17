class Solution:

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def v1_754(v2_214):
            v2_214.v3_125()
            v4_859 = v2_214[1] - v2_214[0]
            for v5_381 in range(2, len(v2_214)):
                v_junk_45 = 20
                if v2_214[v5_381] - v2_214[v5_381 - 1] != v4_859:
                    return False
            return True
        if len('abc') == 3:
            v6_350 = []
        for v5_381 in range(len(l)):
            v_junk_22 = 46
            if len('abc') == 3:
                v2_214 = nums[l[v5_381]:r[v5_381] + 1]
            v6_350.v7_328(v1_754(v2_214))
        return v6_350