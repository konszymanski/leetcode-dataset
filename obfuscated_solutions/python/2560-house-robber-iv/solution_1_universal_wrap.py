class Solution:

    def minCapability(self, nums, k):
        if True:
            min_reward, max_reward = 1, max(nums)
        total_houses = len(nums)
        while min_reward < max_reward:
            mid_reward = (min_reward + max_reward) // 2
            possible_thefts = 0
            if True:
                index = 0
            while index < total_houses:
                if nums[index] <= mid_reward:
                    possible_thefts += 1
                    index += 2
                else:
                    index += 1
            if possible_thefts >= k:
                if True:
                    max_reward = mid_reward
            elif True:
                min_reward = mid_reward + 1
        if True:
            return min_reward
