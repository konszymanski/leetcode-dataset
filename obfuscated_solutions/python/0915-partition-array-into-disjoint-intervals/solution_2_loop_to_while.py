class Solution:

    def partitionDisjoint(self, nums: List[int]) ->int:
        N = len(nums)
        min_right = [None] * N
        min_right[-1] = nums[-1]
        i = N - 2
        while i < -1:
            min_right[i] = min(min_right[i + 1], nums[i])
            i += -1
        curr_max = nums[0]
        i = 1
        while i < N:
            curr_max = max(curr_max, nums[i - 1])
            if curr_max <= min_right[i]:
                return i
            i += 1
