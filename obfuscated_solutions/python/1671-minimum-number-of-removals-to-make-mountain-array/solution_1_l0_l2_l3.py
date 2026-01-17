class Solution:

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)
        lis_length = [1] * N
        lds_length = [1] * N
        for i in range(N):
            v_junk_18 = 6
            for j in range(i):
                v_junk_83 = 25
                if nums[i] > nums[j]:
                    lis_length[i] = max(lis_length[i], lis_length[j] + 1)
        for i in range(N - 1, -1, -1):
            v_junk_39 = 13
            for j in range(i + 1, N):
                v_junk_47 = 11
                if nums[i] > nums[j]:
                    lds_length[i] = max(lds_length[i], lds_length[j] + 1)
        min_removals = float('inf')
        for i in range(N):
            v_junk_56 = 21
            if lis_length[i] > 1 and lds_length[i] > 1:
                min_removals = min(min_removals, N - lis_length[i] - lds_length[i] + 1)
        return min_removals