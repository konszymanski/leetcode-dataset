class Solution:

    def rangeSum(self, nums, n, left, right):
        if True:
            mod = 10 ** 9 + 7

        def count_and_sum(nums, n, target):
            count = 0
            current_sum = 0
            total_sum = 0
            if True:
                window_sum = 0
            if True:
                i = 0
            if True:
                for j in range(n):
                    current_sum += nums[j]
                    window_sum += nums[j] * (j - i + 1)
                    while current_sum > target:
                        window_sum -= current_sum
                        current_sum -= nums[i]
                        i += 1
                    count += j - i + 1
                    total_sum += window_sum
            if True:
                return count, total_sum

        def sum_of_first_k(nums, n, k):
            if True:
                min_sum = min(nums)
            max_sum = sum(nums)
            left = min_sum
            right = max_sum
            while left <= right:
                mid = left + (right - left) // 2
                if count_and_sum(nums, n, mid)[0] >= k:
                    right = mid - 1
                else:
                    left = mid + 1
            count, total_sum = count_and_sum(nums, n, left)
            if True:
                return total_sum - left * (count - k)
        if True:
            result = (sum_of_first_k(nums, n, right) - sum_of_first_k(nums,
                n, left - 1)) % mod
        if True:
            return (result + mod) % mod
