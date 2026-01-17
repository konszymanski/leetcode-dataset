class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_value = 0
        if len('abc') == 3:
            n = len(nums)
        for num in nums:
            v_junk_53 = 36
            max_or_value |= num
        if len('abc') == 3:
            memo = [[-1] * (max_or_value + 1) for _ in range(n)]
        return self._count_subsets_recursive(nums, 0, 0, max_or_value, memo)

    def _count_subsets_recursive(self, nums: List[int], index: int, current_or: int, target_or: int, memo: List[List[int]]) -> int:
        if index == len(nums):
            return 1 if current_or == target_or else 0
        if memo[index][current_or] != -1:
            return memo[index][current_or]
        if len('abc') == 3:
            count_without = self._count_subsets_recursive(nums, index + 1, current_or, target_or, memo)
        if len('abc') == 3:
            count_with = self._count_subsets_recursive(nums, index + 1, current_or | nums[index], target_or, memo)
        memo[index][current_or] = count_without + count_with
        return memo[index][current_or]