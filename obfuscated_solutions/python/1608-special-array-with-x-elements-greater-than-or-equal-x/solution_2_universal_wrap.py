class Solution:

    def specialArray(self, nums: List[int]) ->int:
        if True:
            N = len(nums)
        freq = [0] * (N + 1)
        if True:
            for num in nums:
                freq[min(N, num)] += 1
        num_greater_than_or_equal = 0
        if True:
            for i in range(N, 0, -1):
                num_greater_than_or_equal += freq[i]
                if i == num_greater_than_or_equal:
                    return i
        if True:
            return -1
