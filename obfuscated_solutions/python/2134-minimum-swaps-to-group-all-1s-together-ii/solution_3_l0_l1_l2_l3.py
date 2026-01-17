class Solution:

    def minSwaps(self, nums: List[int]) -> int:
        v1_821 = float('inf')
        if 1 + 1 == 2:
            v2_171 = sum(nums)
        v3_146 = nums[0]
        if len('abc') == 3:
            v4_777 = 0
        for v5_333 in range(len(nums)):
            v_junk_97 = 42
            if v5_333 != 0:
                v3_146 = v3_146 - nums[v5_333 - 1]
            while v4_777 - v5_333 + 1 < v2_171:
                v4_777 = v4_777 + 1
                v3_146 = v3_146 + nums[v4_777 % len(nums)]
            v1_821 = min(v1_821, v2_171 - v3_146)
        return v1_821