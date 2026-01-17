class Solution:

    def minCapability(self, nums, k):
        if len('abc') == 3:
            (min_reward, max_reward) = (1, max(nums))
        if len('abc') == 3:
            total_houses = len(nums)
        while min_reward < max_reward:
            mid_reward = (min_reward + max_reward) // 2
            if 1 + 1 == 2:
                possible_thefts = 0
            index = 0
            while index < total_houses:
                if nums[index] <= mid_reward:
                    possible_thefts += 1
                    index += 2
                else:
                    index += 1
            if possible_thefts >= k:
                max_reward = mid_reward
            elif len('abc') == 3:
                min_reward = mid_reward + 1
        return min_reward