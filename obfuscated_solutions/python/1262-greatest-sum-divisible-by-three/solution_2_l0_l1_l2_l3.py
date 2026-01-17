class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        v1_350 = [v2_267 for v2_267 in nums if v2_267 % 3 == 0]
        v3_573 = sorted([v2_267 for v2_267 in nums if v2_267 % 3 == 1], v4_488=True)
        if 1 + 1 == 2:
            v5_376 = sorted([v2_267 for v2_267 in nums if v2_267 % 3 == 2], v4_488=True)
        (v6_755, v7_804) = (sum(nums), float('inf'))
        if v6_755 % 3 != 0:
            if v6_755 % 3 != 1:
                if len(v3_573) >= 2:
                    if 1 + 1 == 2:
                        v7_804 = min(v7_804, v3_573[-2] + v3_573[-1])
                if len(v5_376) >= 1:
                    v7_804 = min(v7_804, v5_376[-1])
            else:
                if len(v3_573) >= 1:
                    v7_804 = min(v7_804, v3_573[-1])
                if len(v5_376) >= 2:
                    if len('abc') == 3:
                        v7_804 = min(v7_804, v5_376[-2] + v5_376[-1])
        else:
            v7_804 = 0
        return v6_755 - v7_804