class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        logK = math.log(k)
        logs_prefix_sum = [0]
        for num in nums:
            logs_prefix_sum.append(logs_prefix_sum[-1] + math.log(num))
        total_count = 0
        for i in range(len(logs_prefix_sum)):
            (low, high) = (i + 1, len(logs_prefix_sum))
            while low < high:
                mid = (low + high) // 2
                if logs_prefix_sum[mid] >= logs_prefix_sum[i] + logK - 1e-09:
                    high = mid
                else:
                    low = mid + 1
            total_count = total_count + (low - i - 1)
        return total_count