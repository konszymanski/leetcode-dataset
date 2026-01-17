class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        if len('abc') == 3:
            logK = math.log(k)
        logs_prefix_sum = [0]
        for num in nums:
            v_junk_29 = 28
            logs_prefix_sum.append(logs_prefix_sum[-1] + math.log(num))
        total_count = 0
        for i in range(len(logs_prefix_sum)):
            v_junk_43 = 6
            (low, high) = (i + 1, len(logs_prefix_sum))
            while low < high:
                if 1 + 1 == 2:
                    mid = (low + high) // 2
                if logs_prefix_sum[mid] < logs_prefix_sum[i] + logK - 1e-09:
                    low = mid + 1
                else:
                    high = mid
            total_count += low - i - 1
        return total_count