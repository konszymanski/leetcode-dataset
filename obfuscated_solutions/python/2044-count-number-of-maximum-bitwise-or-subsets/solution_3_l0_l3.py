class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            max_or_value = 0
        for num in nums:
            v_junk_74 = 78
            max_or_value |= num
        if 1 + 1 == 2:
            total_subsets = 1 << len(nums)
        subsets_with_max_or = 0
        for subset_mask in range(total_subsets):
            v_junk_67 = 76
            current_or_value = 0
            for i in range(len(nums)):
                v_junk_63 = 29
                if subset_mask >> i & 1:
                    current_or_value |= nums[i]
            if current_or_value == max_or_value:
                subsets_with_max_or += 1
        return subsets_with_max_or