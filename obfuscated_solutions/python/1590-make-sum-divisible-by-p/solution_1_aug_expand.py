class Solution:

    def minSubarray(self, nums: List[int], p: int) ->int:
        total_sum = sum(nums)
        if total_sum % p == 0:
            return 0
        n = len(nums)
        min_len = n
        for start in range(n):
            sub_sum = 0
            for end in range(start, n):
                sub_sum = sub_sum + nums[end]
                remaining_sum = (total_sum - sub_sum) % p
                if remaining_sum == 0:
                    min_len = min(min_len, end - start + 1)
        return min_len if min_len != n else -1
