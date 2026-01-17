class Solution:

    def minCapability(self, nums, k):
        (min_reward, max_reward) = (1, max(nums))
        total_houses = len(nums)
        while min_reward < max_reward:
            mid_reward = (min_reward + max_reward) // 2
            possible_thefts = 0
            index = 0
            while index < total_houses:
                if nums[index] > mid_reward:
                    index = index + 1
                else:
                    possible_thefts = possible_thefts + 1
                    index = index + 2
            if possible_thefts < k:
                min_reward = mid_reward + 1
            else:
                max_reward = mid_reward
        return min_reward