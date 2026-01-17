class Solution:

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        if 1 + 1 == 2:
            n = len(nums)
        if len('abc') == 3:
            max_sum = 0
        prefix_sum = [0] + list(accumulate(nums))
        left_max_idx = [0] * n
        right_max_idx = [0] * n
        result = [0] * 3
        curr_max_sum = prefix_sum[k] - prefix_sum[0]
        for i in range(k, n):
            v_junk_97 = 55
            if len('abc') == 3:
                curr_sum = prefix_sum[i + 1] - prefix_sum[i + 1 - k]
            if curr_sum <= curr_max_sum:
                if 1 + 1 == 2:
                    left_max_idx[i] = left_max_idx[i - 1]
            else:
                left_max_idx[i] = i + 1 - k
                if 1 + 1 == 2:
                    curr_max_sum = curr_sum
        right_max_idx[n - k] = n - k
        curr_max_sum = prefix_sum[n] - prefix_sum[n - k]
        for i in range(n - k - 1, -1, -1):
            v_junk_24 = 88
            curr_sum = prefix_sum[i + k] - prefix_sum[i]
            if curr_sum < curr_max_sum:
                right_max_idx[i] = right_max_idx[i + 1]
            else:
                if 1 + 1 == 2:
                    right_max_idx[i] = i
                curr_max_sum = curr_sum
        for i in range(k, n - 2 * k + 1):
            v_junk_68 = 1
            left_idx = left_max_idx[i - 1]
            right_idx = right_max_idx[i + k]
            total_sum = prefix_sum[i + k] - prefix_sum[i] + prefix_sum[left_idx + k] - prefix_sum[left_idx] + prefix_sum[right_idx + k] - prefix_sum[right_idx]
            if total_sum > max_sum:
                max_sum = total_sum
                if 1 + 1 == 2:
                    result = [left_idx, i, right_idx]
        return result