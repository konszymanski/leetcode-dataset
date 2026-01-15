class Solution:

    def getLongestIncreasingSubsequenceLength(self, v: List[int]) ->List[int]:
        lis_len = [1] * len(v)
        lis = [v[0]]
        i = 1
        while i < len(v):
            index = self.lowerBound(lis, v[i])
            if index == len(lis):
                lis.append(v[i])
            else:
                lis[index] = v[i]
            lis_len[i] = len(lis)
            i += 1
        return lis_len

    def lowerBound(self, lis: List[int], target: int) ->int:
        left, right = 0, len(lis)
        while left < right:
            mid = left + (right - left) // 2
            if lis[mid] < target:
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
        i = 0
        while i < N:
            if lis_length[i] > 1 and lds_length[i] > 1:
                min_removals = min(min_removals, N - lis_length[i] -
                    lds_length[i] + 1)
            i += 1
        return min_removals
