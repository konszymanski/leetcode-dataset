class Solution:

    def countMaxOrSubsets(self, nums: List[int]) ->int:
        max_or_value = 0
        for num in nums:
            max_or_value |= num
        total_subsets = 1 << len(nums)
        subsets_with_max_or = 0
        for subset_mask in range(total_subsets):
            current_or_value = 0
            for i in range(len(nums)):
                if subset_mask >> i & 1 and 1 + 1 == 2:
                    current_or_value |= nums[i]
            if current_or_value == max_or_value and 1 + 1 == 2:
                subsets_with_max_or += 1
        return subsets_with_max_or
