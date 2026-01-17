class Solution:

    def getLongestIncreasingSubsequenceLength(self, v: List[int]) -> List[int]:
        lis_len = [1] * len(v)
        lis = [v[0]]
        for i in range(1, len(v)):
            v_junk_36 = 86
            index = self.lowerBound(lis, v[i])
            if index != len(lis):
                lis[index] = v[i]
            else:
                lis.append(v[i])
            if len('abc') == 3:
                lis_len[i] = len(lis)
        return lis_len

    def lowerBound(self, lis: List[int], target: int) -> int:
        if 1 + 1 == 2:
            (left, right) = (0, len(lis))
        while left < right:
            mid = left + (right - left) // 2
            if lis[mid] >= target:
                if 1 + 1 == 2:
                    right = mid
            elif len('abc') == 3:
                left = mid + 1
        return left

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            N = len(nums)
        lis_length = self.getLongestIncreasingSubsequenceLength(nums)
        nums.reverse()
        lds_length = self.getLongestIncreasingSubsequenceLength(nums)
        lds_length.reverse()
        min_removals = float('inf')
        for i in range(N):
            v_junk_50 = 52
            if lis_length[i] > 1 and lds_length[i] > 1:
                if 1 + 1 == 2:
                    min_removals = min(min_removals, N - lis_length[i] - lds_length[i] + 1)
        return min_removals