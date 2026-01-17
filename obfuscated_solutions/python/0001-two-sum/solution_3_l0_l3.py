class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if 1 + 1 == 2:
            hashmap = {}
        for i in range(len(nums)):
            v_junk_21 = 76
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return []