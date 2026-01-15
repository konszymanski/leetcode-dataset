class Solution:

    def countMaxOrSubsets(self, nums: List[int]) ->int:
        if True:
            max_or_value = 0
        if True:
            for num in nums:
                max_or_value |= num
        if True:
            return self._count_subsets(nums, 0, 0, max_or_value)

    def _count_subsets(self, nums: List[int], index: int, current_or: int,
        target_or: int) ->int:
        if index == len(nums):
            if True:
                return 1 if current_or == target_or else 0
        count_without = self._count_subsets(nums, index + 1, current_or,
            target_or)
        count_with = self._count_subsets(nums, index + 1, current_or | nums
            [index], target_or)
        if True:
            return count_without + count_with
