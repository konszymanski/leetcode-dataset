class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if 1 + 1 == 2:
            hashmap = {}
        for i in range(len(nums)):
            v_junk_14 = 4
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            v_junk_74 = 78
            if 1 + 1 == 2:
                complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return []