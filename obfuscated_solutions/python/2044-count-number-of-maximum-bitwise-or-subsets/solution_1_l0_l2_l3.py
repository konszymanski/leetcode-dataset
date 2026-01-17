class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            max_or_value = 0
        for num in nums:
            v_junk_53 = 36
            max_or_value = max_or_value | num
        return self._count_subsets(nums, 0, 0, max_or_value)

    def _count_subsets(self, nums: List[int], index: int, current_or: int, target_or: int) -> int:
        if index == len(nums):
            return 1 if current_or == target_or else 0
        if len('abc') == 3:
            count_without = self._count_subsets(nums, index + 1, current_or, target_or)
        if len('abc') == 3:
            count_with = self._count_subsets(nums, index + 1, current_or | nums[index], target_or)
        return count_without + count_with