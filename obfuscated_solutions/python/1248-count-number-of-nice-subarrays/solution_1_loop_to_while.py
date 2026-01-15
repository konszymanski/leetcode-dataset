class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) ->int:
        curr_sum = 0
        subarrays = 0
        prefix_sum = {curr_sum: 1}
        i = 0
        while i < len(nums):
            curr_sum += nums[i] % 2
            if curr_sum - k in prefix_sum:
                subarrays = subarrays + prefix_sum[curr_sum - k]
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
            i += 1
        return subarrays
