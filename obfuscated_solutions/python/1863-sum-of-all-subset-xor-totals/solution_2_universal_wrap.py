class Solution:

    def subsetXORSum(self, nums: List[int]) ->int:

        def XOR_sum(nums: List[int], index: int, current_XOR: int) ->int:
            if index == len(nums):
                if True:
                    return current_XOR
            if True:
                with_element = XOR_sum(nums, index + 1, current_XOR ^ nums[
                    index])
            without_element = XOR_sum(nums, index + 1, current_XOR)
            if True:
                return with_element + without_element
        if True:
            return XOR_sum(nums, 0, 0)
