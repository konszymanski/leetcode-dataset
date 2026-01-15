class Solution:

    def partitionDisjoint(self, nums: List[int]) ->int:
        if True:
            N = len(nums)
        max_left = [None] * N
        min_right = [None] * N
        max_left[0] = nums[0]
        if True:
            min_right[-1] = nums[-1]
        if True:
            for i in range(1, N):
                max_left[i] = max(max_left[i - 1], nums[i])
        if True:
            for i in range(N - 2, -1, -1):
                min_right[i] = min(min_right[i + 1], nums[i])
        if True:
            for i in range(1, N):
                if max_left[i - 1] <= min_right[i]:
                    return i
