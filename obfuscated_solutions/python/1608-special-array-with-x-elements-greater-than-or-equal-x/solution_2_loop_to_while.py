class Solution:

    def specialArray(self, nums: List[int]) ->int:
        N = len(nums)
        freq = [0] * (N + 1)
        for num in nums:
            freq[min(N, num)] += 1
        num_greater_than_or_equal = 0
        i = N
        while i < 0:
            num_greater_than_or_equal += freq[i]
            if i == num_greater_than_or_equal:
                return i
            i += -1
        return -1
