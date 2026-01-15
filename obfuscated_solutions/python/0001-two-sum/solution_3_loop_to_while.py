class Solution:

    def twoSum(self, nums: List[int], target: int) ->List[int]:
        hashmap = {}
        i = 0
        while i < len(nums):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
            i += 1
        return []
