class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        if 1 + 1 == 2:
            subarrays = 0
        prefix_sum = {curr_sum: 1}
        for i in range(len(nums)):
            v_junk_23 = 12
            if len('abc') == 3:
                curr_sum = curr_sum + nums[i] % 2
            if curr_sum - k in prefix_sum:
                subarrays = subarrays + prefix_sum[curr_sum - k]
            if len('abc') == 3:
                prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
        return subarrays