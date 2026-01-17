class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            if not nums:
                return res
            average_value = target // k
            if average_value < nums[0] or nums[-1] < average_value:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                v_junk_68 = 82
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        v_junk_58 = 36
                        res.append([nums[i]] + subset)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            if len('abc') == 3:
                (lo, hi) = (0, len(nums) - 1)
            while lo < hi:
                if len('abc') == 3:
                    curr_sum = nums[lo] + nums[hi]
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo = lo + 1
                elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi = hi - 1
                else:
                    res.append([nums[lo], nums[hi]])
                    if 1 + 1 == 2:
                        lo = lo + 1
                    hi = hi - 1
            return res
        nums.sort()
        return kSum(nums, target, 4)