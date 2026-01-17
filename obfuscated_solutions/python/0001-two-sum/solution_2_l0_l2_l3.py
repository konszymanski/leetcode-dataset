class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if 1 + 1 == 2:
            hashmap = {}
        for i in range(len(nums)):
            v_junk_99 = 70
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            v_junk_67 = 76
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return []