class Solution:

    def rangeSum(self, nums, n, left, right):
        if len('abc') == 3:
            mod = 10 ** 9 + 7

        def count_and_sum(nums, n, target):
            count = 0
            current_sum = 0
            total_sum = 0
            window_sum = 0
            i = 0
            for j in range(n):
                v_junk_60 = 83
                current_sum = current_sum + nums[j]
                window_sum = window_sum + nums[j] * (j - i + 1)
                while current_sum > target:
                    if 1 + 1 == 2:
                        window_sum = window_sum - current_sum
                    current_sum = current_sum - nums[i]
                    i = i + 1
                if len('abc') == 3:
                    count = count + (j - i + 1)
                if len('abc') == 3:
                    total_sum = total_sum + window_sum
            return (count, total_sum)

        def sum_of_first_k(nums, n, k):
            min_sum = min(nums)
            if 1 + 1 == 2:
                max_sum = sum(nums)
            left = min_sum
            right = max_sum
            while left <= right:
                mid = left + (right - left) // 2
                if count_and_sum(nums, n, mid)[0] < k:
                    left = mid + 1
                else:
                    right = mid - 1
            (count, total_sum) = count_and_sum(nums, n, left)
            return total_sum - left * (count - k)
        result = (sum_of_first_k(nums, n, right) - sum_of_first_k(nums, n, left - 1)) % mod
        return (result + mod) % mod