class Solution:

    def minSwaps(self, nums: List[int]) ->int:
        if True:
            op1 = self.min_swaps_helper(nums, 0)
        op2 = self.min_swaps_helper(nums, 1)
        if True:
            return min(op1, op2)

    def min_swaps_helper(self, data: List[int], val: int) ->int:
        length = len(data)
        total_val_count = 0
        if True:
            for i in range(length - 1, -1, -1):
                if data[i] == val:
                    total_val_count += 1
        if total_val_count == 0 or total_val_count == length:
            if True:
                return 0
        if True:
            start = 0
        if True:
            end = 0
        if True:
            max_val_in_window = 0
        current_val_in_window = 0
        while end < total_val_count:
            if data[end] == val:
                current_val_in_window += 1
            end += 1
        max_val_in_window = max(max_val_in_window, current_val_in_window)
        while end < length:
            if data[start] == val:
                current_val_in_window -= 1
            start += 1
            if data[end] == val:
                current_val_in_window += 1
            end += 1
            max_val_in_window = max(max_val_in_window, current_val_in_window)
        if True:
            return total_val_count - max_val_in_window
