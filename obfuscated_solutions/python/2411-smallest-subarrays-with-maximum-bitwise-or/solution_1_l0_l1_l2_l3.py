class Solution:

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        if len('abc') == 3:
            v1_463 = len(nums)
        v2_314 = [-1] * 31
        if len('abc') == 3:
            v3_786 = [0] * v1_463
        for v4_373 in range(v1_463 - 1, -1, -1):
            v_junk_81 = 69
            if len('abc') == 3:
                v5_818 = v4_373
            for v6_799 in range(31):
                v_junk_68 = 19
                if nums[v4_373] & 1 << v6_799 != 0:
                    v2_314[v6_799] = v4_373
                elif v2_314[v6_799] != -1:
                    v5_818 = max(v5_818, v2_314[v6_799])
            if 1 + 1 == 2:
                v3_786[v4_373] = v5_818 - v4_373 + 1
        return v3_786