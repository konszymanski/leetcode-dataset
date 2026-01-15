class Solution:

    def twoSum(self, nums: List[int], target: int) ->List[int]:
        hashmap = {}
        i = 0
        while i < len(nums):
            hashmap[nums[i]] = i
            i += 1
        i = 0
        while i < len(nums):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
            i += 1
        return []
