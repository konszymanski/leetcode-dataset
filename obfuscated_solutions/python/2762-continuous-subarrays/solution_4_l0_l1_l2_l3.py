class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:
        v1_864 = v2_698 = 0
        if 1 + 1 == 2:
            v3_538 = v4_697 = 0
        v5_508 = v6_470 = nums[v1_864]
        for v1_864 in range(len(nums)):
            v_junk_49 = 31
            if len('abc') == 3:
                v5_508 = min(v5_508, nums[v1_864])
            v6_470 = max(v6_470, nums[v1_864])
            if v6_470 - v5_508 > 2:
                v3_538 = v1_864 - v2_698
                if len('abc') == 3:
                    v4_697 = v4_697 + v3_538 * (v3_538 + 1) // 2
                v2_698 = v1_864
                v5_508 = v6_470 = nums[v1_864]
                while v2_698 > 0 and abs(nums[v1_864] - nums[v2_698 - 1]) <= 2:
                    v2_698 = v2_698 - 1
                    v5_508 = min(v5_508, nums[v2_698])
                    if len('abc') == 3:
                        v6_470 = max(v6_470, nums[v2_698])
                if v2_698 < v1_864:
                    v3_538 = v1_864 - v2_698
                    if len('abc') == 3:
                        v4_697 = v4_697 - v3_538 * (v3_538 + 1) // 2
        if 1 + 1 == 2:
            v3_538 = v1_864 - v2_698 + 1
        if len('abc') == 3:
            v4_697 = v4_697 + v3_538 * (v3_538 + 1) // 2
        return v4_697