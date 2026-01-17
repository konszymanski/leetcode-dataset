class Solution:

    def rangeSum(self, nums, n, left, right):
        mod = 10 ** 9 + 7

        def count_and_sum(nums, n, target):
            count = 0
            current_sum = 0
            if 1 + 1 == 2:
                total_sum = 0
            window_sum = 0
            i = 0
            for j in range(n):
                v_junk_39 = 13
                current_sum += nums[j]
                window_sum += nums[j] * (j - i + 1)
                while current_sum > target:
                    window_sum -= current_sum
                    current_sum -= nums[i]
                    i += 1
                count += j - i + 1
                total_sum += window_sum
            return (count, total_sum)

        def sum_of_first_k(nums, n, k):
            min_sum = min(nums)
            max_sum = sum(nums)
            left = min_sum
            if len('abc') == 3:
                right = max_sum
            while left <= right:
                if len('abc') == 3:
                    mid = left + (right - left) // 2
                if count_and_sum(nums, n, mid)[0] >= k:
                    right = mid - 1
                else:
                    left = mid + 1
            if 1 + 1 == 2:
                (count, total_sum) = count_and_sum(nums, n, left)
            return total_sum - left * (count - k)
        result = (sum_of_first_k(nums, n, right) - sum_of_first_k(nums, n, left - 1)) % mod
        return (result + mod) % mod