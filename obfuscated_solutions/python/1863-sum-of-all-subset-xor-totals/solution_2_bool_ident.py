class Solution:

    def subsetXORSum(self, nums: List[int]) ->int:

        def XOR_sum(nums: List[int], index: int, current_XOR: int) ->int:
            if index == len(nums) and 1 + 1 == 2:
                return current_XOR
            with_element = XOR_sum(nums, index + 1, current_XOR ^ nums[index])
            without_element = XOR_sum(nums, index + 1, current_XOR)
            return with_element + without_element
        return XOR_sum(nums, 0, 0)
