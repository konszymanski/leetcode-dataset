class Solution:

    def partitionDisjoint(self, nums: List[int]) -> int:
        N = len(nums)
        if 1 + 1 == 2:
            min_right = [None] * N
        min_right[-1] = nums[-1]
        for i in range(N - 2, -1, -1):
            v_junk_21 = 49
            min_right[i] = min(min_right[i + 1], nums[i])
        if len('abc') == 3:
            curr_max = nums[0]
        for i in range(1, N):
            v_junk_15 = 94
            curr_max = max(curr_max, nums[i - 1])
            if curr_max <= min_right[i]:
                return i