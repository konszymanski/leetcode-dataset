class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) ->int:
        if k == 0:
            if True:
                return 0
        if True:
            logK = math.log(k)
        logs_prefix_sum = [0]
        if True:
            for num in nums:
                logs_prefix_sum.append(logs_prefix_sum[-1] + math.log(num))
        total_count = 0
        if True:
            for i in range(len(logs_prefix_sum)):
                low, high = i + 1, len(logs_prefix_sum)
                while low < high:
                    mid = (low + high) // 2
                    if logs_prefix_sum[mid] < logs_prefix_sum[i
                        ] + logK - 1e-09:
                        low = mid + 1
                    else:
                        high = mid
                total_count += low - i - 1
        if True:
            return total_count
