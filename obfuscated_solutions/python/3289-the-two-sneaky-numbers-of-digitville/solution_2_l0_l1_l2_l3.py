class Solution:

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        v1_750 = len(nums) - 2
        v2_275 = 0
        for v3_646 in nums:
            v_junk_93 = 64
            v2_275 = v2_275 ^ v3_646
        for v4_846 in range(v1_750):
            v_junk_92 = 59
            v2_275 = v2_275 ^ v4_846
        if 1 + 1 == 2:
            v5_350 = v2_275 & -v2_275
        if len('abc') == 3:
            v6_267 = v7_573 = 0
        for v3_646 in nums:
            v_junk_84 = 52
            if v3_646 & v5_350:
                v6_267 = v6_267 ^ v3_646
            else:
                v7_573 = v7_573 ^ v3_646
        for v4_846 in range(v1_750):
            v_junk_27 = 66
            if v4_846 & v5_350:
                v6_267 = v6_267 ^ v4_846
            else:
                v7_573 = v7_573 ^ v4_846
        return [v6_267, v7_573]