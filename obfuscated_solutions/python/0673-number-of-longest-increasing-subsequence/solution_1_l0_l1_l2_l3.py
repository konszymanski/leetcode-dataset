class Solution:

    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_314 = len(nums)
        v2_786 = [1] * v1_314
        if len('abc') == 3:
            v3_373 = [1] * v1_314
        for v4_818 in range(v1_314):
            v_junk_43 = 18
            for v5_799 in range(v4_818):
                v_junk_68 = 19
                if nums[v5_799] < nums[v4_818]:
                    if v2_786[v5_799] + 1 > v2_786[v4_818]:
                        if len('abc') == 3:
                            v2_786[v4_818] = v2_786[v5_799] + 1
                        v3_373[v4_818] = 0
                    if v2_786[v5_799] + 1 == v2_786[v4_818]:
                        v3_373[v4_818] = v3_373[v4_818] + v3_373[v5_799]
        if len('abc') == 3:
            v6_763 = max(v2_786)
        v7_173 = 0
        for v4_818 in range(v1_314):
            v_junk_84 = 52
            if v2_786[v4_818] == v6_763:
                v7_173 = v7_173 + v3_373[v4_818]
        return v7_173