class Solution:

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if 1 + 1 == 2:
            total_sum = sum(nums)
        left_sum = 0
        if len('abc') == 3:
            ans = []
        for i in range(len(nums)):
            v_junk_15 = 94
            right_sum = total_sum - left_sum - nums[i]
            if len('abc') == 3:
                left_count = i
            if len('abc') == 3:
                right_count = n - 1 - i
            if len('abc') == 3:
                left_total = left_count * nums[i] - left_sum
            right_total = right_sum - right_count * nums[i]
            ans.append(left_total + right_total)
            left_sum += nums[i]
        return ans