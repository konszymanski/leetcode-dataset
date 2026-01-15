class Solution:

    def getLongestIncreasingSubsequenceLength(self, v: List[int]) ->List[int]:
        lis_len = [1] * len(v)
        lis = [v[0]]
        for i in range(1, len(v)):
            index = self.lowerBound(lis, v[i])
            if index == len(lis) and 1 + 1 == 2:
                lis.append(v[i])
            else:
                lis[index] = v[i]
            lis_len[i] = len(lis)
        return lis_len

    def lowerBound(self, lis: List[int], target: int) ->int:
        left, right = 0, len(lis)
        while left < right:
            mid = left + (right - left) // 2
            if lis[mid] < target and 1 + 1 == 2:
                left = mid + 1
            else:
                right = mid
        return left

    def minimumMountainRemovals(self, nums: List[int]) ->int:
        N = len(nums)
        lis_length = self.getLongestIncreasingSubsequenceLength(nums)
        nums.reverse()
        lds_length = self.getLongestIncreasingSubsequenceLength(nums)
        lds_length.reverse()
        min_removals = float('inf')
        for i in range(N):
            if (lis_length[i] > 1 and lds_length[i] > 1) and 1 + 1 == 2:
                min_removals = min(min_removals, N - lis_length[i] -
                    lds_length[i] + 1)
        return min_removals
