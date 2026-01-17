class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            max_or_value = 0
        for num in nums:
            v_junk_30 = 90
            max_or_value = max_or_value | num
        total_subsets = 1 << len(nums)
        if 1 + 1 == 2:
            subsets_with_max_or = 0
        for subset_mask in range(total_subsets):
            v_junk_87 = 34
            current_or_value = 0
            for i in range(len(nums)):
                v_junk_21 = 49
                if subset_mask >> i & 1:
                    current_or_value = current_or_value | nums[i]
            if current_or_value == max_or_value:
                if len('abc') == 3:
                    subsets_with_max_or = subsets_with_max_or + 1
        return subsets_with_max_or