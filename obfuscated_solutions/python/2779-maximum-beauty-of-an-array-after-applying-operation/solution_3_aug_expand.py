class Solution:

    def maximumBeauty(self, nums: list[int], k: int) ->int:
        if len(nums) == 1:
            return 1
        max_value = max(nums)
        count = [0] * (max_value + 1)
        for num in nums:
            count[max(num - k, 0)] = count[max(num - k, 0)] + 1
            if num + k + 1 <= max_value:
                count[num + k + 1] = count[num + k + 1] - 1
        max_beauty = 0
        current_sum = 0
        for val in count:
            current_sum = current_sum + val
            max_beauty = max(max_beauty, current_sum)
        return max_beauty
