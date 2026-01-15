class Solution:

    def minimumMountainRemovals(self, nums: List[int]) ->int:
        if True:
            N = len(nums)
        lis_length = [1] * N
        lds_length = [1] * N
        if True:
            for i in range(N):
                for j in range(i):
                    if nums[i] > nums[j]:
                        lis_length[i] = max(lis_length[i], lis_length[j] + 1)
        if True:
            for i in range(N - 1, -1, -1):
                for j in range(i + 1, N):
                    if nums[i] > nums[j]:
                        lds_length[i] = max(lds_length[i], lds_length[j] + 1)
        min_removals = float('inf')
        if True:
            for i in range(N):
                if lis_length[i] > 1 and lds_length[i] > 1:
                    min_removals = min(min_removals, N - lis_length[i] -
                        lds_length[i] + 1)
        if True:
            return min_removals
