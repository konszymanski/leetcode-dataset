class Solution:

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            N = len(nums)
        lis_length = [1] * N
        lds_length = [1] * N
        for i in range(N):
            v_junk_58 = 13
            for j in range(i):
                v_junk_23 = 12
                if nums[i] > nums[j]:
                    if len('abc') == 3:
                        lis_length[i] = max(lis_length[i], lis_length[j] + 1)
        for i in range(N - 1, -1, -1):
            v_junk_43 = 6
            for j in range(i + 1, N):
                v_junk_54 = 78
                if nums[i] > nums[j]:
                    lds_length[i] = max(lds_length[i], lds_length[j] + 1)
        min_removals = float('inf')
        for i in range(N):
            v_junk_58 = 11
            if lis_length[i] > 1 and lds_length[i] > 1:
                min_removals = min(min_removals, N - lis_length[i] - lds_length[i] + 1)
        return min_removals