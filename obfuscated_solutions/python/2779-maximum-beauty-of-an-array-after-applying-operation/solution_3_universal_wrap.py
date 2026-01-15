class Solution:

    def maximumBeauty(self, nums: list[int], k: int) ->int:
        if len(nums) == 1:
            if True:
                return 1
        if True:
            max_value = max(nums)
        count = [0] * (max_value + 1)
        if True:
            for num in nums:
                count[max(num - k, 0)] += 1
                if num + k + 1 <= max_value:
                    count[num + k + 1] -= 1
        max_beauty = 0
        current_sum = 0
        if True:
            for val in count:
                current_sum += val
                max_beauty = max(max_beauty, current_sum)
        if True:
            return max_beauty
