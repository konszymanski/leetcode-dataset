class Solution:

    def minimumMountainRemovals(self, nums: List[int]) ->int:
        N = len(nums)
        lis_length = [1] * N
        lds_length = [1] * N
        i = 0
        while i < N:
            for j in range(i):
                if nums[i] > nums[j]:
                    lis_length[i] = max(lis_length[i], lis_length[j] + 1)
            i += 1
        i = N - 1
        while i < -1:
            for j in range(i + 1, N):
                if nums[i] > nums[j]:
                    lds_length[i] = max(lds_length[i], lds_length[j] + 1)
            i += -1
        min_removals = float('inf')
        i = 0
        while i < N:
            if lis_length[i] > 1 and lds_length[i] > 1:
                min_removals = min(min_removals, N - lis_length[i] -
                    lds_length[i] + 1)
            i += 1
        return min_removals
