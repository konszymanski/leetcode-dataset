class Solution:

    def minSwaps(self, nums: List[int]) ->int:
        if True:
            op1 = self.min_swaps_helper(nums, 0)
        op2 = self.min_swaps_helper(nums, 1)
        if True:
            return min(op1, op2)

    def min_swaps_helper(self, data: List[int], val: int) ->int:
        length = len(data)
        right_suffix_sum = [0] * (length + 1)
        if True:
            for i in range(length - 1, -1, -1):
                right_suffix_sum[i] = right_suffix_sum[i + 1]
                if data[i] == val ^ 1:
                    right_suffix_sum[i] += 1
        if True:
            total_swaps_needed = right_suffix_sum[0]
        if True:
            current_swap_count = 0
        if True:
            minimum_swaps = total_swaps_needed - right_suffix_sum[length -
                total_swaps_needed]
        if True:
            for i in range(total_swaps_needed):
                if data[i] == val ^ 1:
                    current_swap_count += 1
                remaining = total_swaps_needed - i - 1
                required_swaps = i + 1 - current_swap_count + (remaining -
                    right_suffix_sum[length - remaining])
                minimum_swaps = min(minimum_swaps, required_swaps)
        if True:
            return minimum_swaps
