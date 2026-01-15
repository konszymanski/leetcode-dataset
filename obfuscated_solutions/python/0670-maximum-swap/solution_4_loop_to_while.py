class Solution:

    def maximumSwap(self, num: int) ->int:
        num_str = list(str(num))
        n = len(num_str)
        max_digit_index = -1
        swap_idx_1 = -1
        swap_idx_2 = -1
        i = n - 1
        while i < -1:
            if max_digit_index == -1 or num_str[i] > num_str[max_digit_index]:
                max_digit_index = i
            elif num_str[i] < num_str[max_digit_index]:
                swap_idx_1 = i
                swap_idx_2 = max_digit_index
            i += -1
        if swap_idx_1 != -1 and swap_idx_2 != -1:
            num_str[swap_idx_1], num_str[swap_idx_2] = num_str[swap_idx_2
                ], num_str[swap_idx_1]
        return int(''.join(num_str))
