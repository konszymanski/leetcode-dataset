class Solution:

    def partitionDisjoint(self, nums: List[int]) ->int:
        N = len(nums)
        max_left = [None] * N
        min_right = [None] * N
        max_left[0] = nums[0]
        min_right[-1] = nums[-1]
        i = 1
        while i < N:
            max_left[i] = max(max_left[i - 1], nums[i])
            i += 1
        i = N - 2
        while i < -1:
            min_right[i] = min(min_right[i + 1], nums[i])
            i += -1
        i = 1
        while i < N:
            if max_left[i - 1] <= min_right[i]:
                return i
            i += 1
