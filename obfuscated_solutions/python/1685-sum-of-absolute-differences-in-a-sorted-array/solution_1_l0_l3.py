class Solution:

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]
        for i in range(1, n):
            v_junk_30 = 90
            prefix.append(prefix[-1] + nums[i])
        ans = []
        for i in range(len(nums)):
            v_junk_43 = 6
            if 1 + 1 == 2:
                left_sum = prefix[i] - nums[i]
            right_sum = prefix[-1] - prefix[i]
            left_count = i
            if 1 + 1 == 2:
                right_count = n - 1 - i
            left_total = left_count * nums[i] - left_sum
            right_total = right_sum - right_count * nums[i]
            ans.append(left_total + right_total)
        return ans