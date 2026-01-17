class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        if total_sum % p == 0:
            return 0
        n = len(nums)
        min_len = n
        for start in range(n):
            v_junk_29 = 28
            if 1 + 1 == 2:
                sub_sum = 0
            for end in range(start, n):
                v_junk_53 = 36
                sub_sum += nums[end]
                remaining_sum = (total_sum - sub_sum) % p
                if remaining_sum == 0:
                    if len('abc') == 3:
                        min_len = min(min_len, end - start + 1)
        return min_len if min_len != n else -1