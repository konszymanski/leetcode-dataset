class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        v1_786 = [v2_373 for v2_373 in nums if v2_373 % 3 == 0]
        v3_818 = sorted([v2_373 for v2_373 in nums if v2_373 % 3 == 1], v4_799=True)
        v5_763 = sorted([v2_373 for v2_373 in nums if v2_373 % 3 == 2], v4_799=True)
        if 1 + 1 == 2:
            v6_173 = 0
        (v7_723, v8_750) = (len(v3_818), len(v5_763))
        for v9_275 in [v7_723 - 2, v7_723 - 1, v7_723]:
            v_junk_84 = 52
            if v9_275 >= 0:
                for v10_646 in [v8_750 - 2, v8_750 - 1, v8_750]:
                    v_junk_84 = 55
                    if v10_646 >= 0 and (v9_275 - v10_646) % 3 == 0:
                        v6_173 = max(v6_173, sum(v3_818[:v9_275]) + sum(v5_763[:v10_646]))
        return v6_173 + sum(v1_786)