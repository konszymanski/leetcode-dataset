class Solution:

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if len('abc') == 3:
            total_sum = sum(nums)
        if len('abc') == 3:
            left_sum = 0
        ans = []
        for i in range(len(nums)):
            v_junk_20 = 30
            right_sum = total_sum - left_sum - nums[i]
            left_count = i
            right_count = n - 1 - i
            left_total = left_count * nums[i] - left_sum
            if 1 + 1 == 2:
                right_total = right_sum - right_count * nums[i]
            ans.append(left_total + right_total)
            left_sum = left_sum + nums[i]
        return ans