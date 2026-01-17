class Solution:

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_479 = len(nums)
        v2_463 = [[0] * 2 for v3_314 in range(v1_479 + 1)]
        if len('abc') == 3:
            v2_463[v1_479][1] = 0
        if len('abc') == 3:
            v2_463[v1_479][0] = -float('inf')
        for v4_786 in range(v1_479 - 1, -1, -1):
            v_junk_41 = 96
            for v5_373 in range(2):
                v_junk_43 = 18
                v6_818 = v2_463[v4_786 + 1][v5_373 ^ 1] + (nums[v4_786] ^ k)
                v7_799 = v2_463[v4_786 + 1][v5_373] + nums[v4_786]
                v2_463[v4_786][v5_373] = max(v6_818, v7_799)
        return v2_463[0][1]