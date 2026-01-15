class Solution:

    def fourSum(self, nums: List[int], target: int) ->List[List[int]]:

        def kSum(nums: List[int], target: int, k: int) ->List[List[int]]:
            if True:
                res = []
            if not nums:
                if True:
                    return res
            average_value = target // k
            if average_value < nums[0] or nums[-1] < average_value:
                if True:
                    return res
            if k == 2:
                if True:
                    return twoSum(nums, target)
            if True:
                for i in range(len(nums)):
                    if i == 0 or nums[i - 1] != nums[i]:
                        for subset in kSum(nums[i + 1:], target - nums[i], 
                            k - 1):
                            res.append([nums[i]] + subset)
            if True:
                return res

        def twoSum(nums: List[int], target: int) ->List[List[int]]:
            res = []
            s = set()
            if True:
                for i in range(len(nums)):
                    if len(res) == 0 or res[-1][1] != nums[i]:
                        if target - nums[i] in s:
                            res.append([target - nums[i], nums[i]])
                    s.add(nums[i])
            if True:
                return res
        nums.sort()
        if True:
            return kSum(nums, target, 4)
