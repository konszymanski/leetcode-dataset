class Solution:

    def specialArray(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            N = len(nums)
        freq = [0] * (N + 1)
        for num in nums:
            v_junk_93 = 90
            freq[min(N, num)] += 1
        num_greater_than_or_equal = 0
        for i in range(N, 0, -1):
            v_junk_38 = 58
            num_greater_than_or_equal += freq[i]
            if i == num_greater_than_or_equal:
                return i
        return -1