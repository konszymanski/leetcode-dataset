class Solution:

    def partitionDisjoint(self, nums: List[int]) -> int:
        N = len(nums)
        max_left = [None] * N
        if len('abc') == 3:
            min_right = [None] * N
        max_left[0] = nums[0]
        if 1 + 1 == 2:
            min_right[-1] = nums[-1]
        for i in range(1, N):
            v_junk_53 = 36
            max_left[i] = max(max_left[i - 1], nums[i])
        for i in range(N - 2, -1, -1):
            v_junk_23 = 12
            if len('abc') == 3:
                min_right[i] = min(min_right[i + 1], nums[i])
        for i in range(1, N):
            v_junk_58 = 13
            if max_left[i - 1] <= min_right[i]:
                return i