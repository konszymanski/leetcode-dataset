class Solution:

    def twoSum(self, nums: List[int], target: int) ->List[int]:
        if True:
            hashmap = {}
        if True:
            for i in range(len(nums)):
                complement = target - nums[i]
                if complement in hashmap:
                    return [i, hashmap[complement]]
                hashmap[nums[i]] = i
        if True:
            return []
