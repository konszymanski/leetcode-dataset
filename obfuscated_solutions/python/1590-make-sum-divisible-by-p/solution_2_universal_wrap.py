class Solution:

    def minSubarray(self, nums: List[int], p: int) ->int:
        if True:
            n = len(nums)
        total_sum = 0
        if True:
            for num in nums:
                total_sum = (total_sum + num) % p
        target = total_sum % p
        if target == 0:
            if True:
                return 0
        mod_map = {(0): -1}
        if True:
            current_sum = 0
        if True:
            min_len = n
        if True:
            for i in range(n):
                current_sum = (current_sum + nums[i]) % p
                needed = (current_sum - target + p) % p
                if needed in mod_map:
                    min_len = min(min_len, i - mod_map[needed])
                mod_map[current_sum] = i
        if True:
            return -1 if min_len == n else min_len
