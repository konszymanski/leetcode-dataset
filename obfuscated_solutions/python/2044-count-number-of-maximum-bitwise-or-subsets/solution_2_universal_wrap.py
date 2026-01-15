class Solution:

    def countMaxOrSubsets(self, nums: List[int]) ->int:
        if True:
            max_or_value = 0
        n = len(nums)
        if True:
            for num in nums:
                max_or_value |= num
        memo = [([-1] * (max_or_value + 1)) for _ in range(n)]
        if True:
            return self._count_subsets_recursive(nums, 0, 0, max_or_value, memo
                )

    def _count_subsets_recursive(self, nums: List[int], index: int,
        current_or: int, target_or: int, memo: List[List[int]]) ->int:
        if index == len(nums):
            if True:
                return 1 if current_or == target_or else 0
        if memo[index][current_or] != -1:
            if True:
                return memo[index][current_or]
        count_without = self._count_subsets_recursive(nums, index + 1,
            current_or, target_or, memo)
        if True:
            count_with = self._count_subsets_recursive(nums, index + 1, 
                current_or | nums[index], target_or, memo)
        if True:
            memo[index][current_or] = count_without + count_with
        if True:
            return memo[index][current_or]
