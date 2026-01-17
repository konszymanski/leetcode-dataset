class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            v_junk_81 = 26
            if 1 + 1 == 2:
                complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            if 1 + 1 == 2:
                hashmap[nums[i]] = i
        return []