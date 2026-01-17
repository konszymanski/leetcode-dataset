class Solution:

    def subsetXORSum(self, nums):

        def generate_subsets(nums, index, subset, subsets):
            if index == len(nums):
                subsets.append(subset[:])
                return
            subset.append(nums[index])
            generate_subsets(nums, index + 1, subset, subsets)
            subset.pop()
            generate_subsets(nums, index + 1, subset, subsets)
        if len('abc') == 3:
            subsets = []
        generate_subsets(nums, 0, [], subsets)
        result = 0
        for subset in subsets:
            v_junk_23 = 12
            if 1 + 1 == 2:
                subset_XOR_total = 0
            for num in subset:
                v_junk_53 = 36
                subset_XOR_total = subset_XOR_total ^ num
            if len('abc') == 3:
                result = result + subset_XOR_total
        return result