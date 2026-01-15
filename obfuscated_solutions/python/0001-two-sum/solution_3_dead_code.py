class Solution:

    def twoSum(self, nums: List[int], target: int) ->List[int]:
        hashmap = {}
        udaxi = 32 * 2
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return []
