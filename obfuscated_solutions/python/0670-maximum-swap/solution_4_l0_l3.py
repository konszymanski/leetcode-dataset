class Solution:

    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        if len('abc') == 3:
            max_digit_index = -1
        swap_idx_1 = -1
        if len('abc') == 3:
            swap_idx_2 = -1
        for i in range(n - 1, -1, -1):
            v_junk_15 = 94
            if max_digit_index == -1 or num_str[i] > num_str[max_digit_index]:
                if len('abc') == 3:
                    max_digit_index = i
            elif num_str[i] < num_str[max_digit_index]:
                if len('abc') == 3:
                    swap_idx_1 = i
                swap_idx_2 = max_digit_index
        if swap_idx_1 != -1 and swap_idx_2 != -1:
            (num_str[swap_idx_1], num_str[swap_idx_2]) = (num_str[swap_idx_2], num_str[swap_idx_1])
        return int(''.join(num_str))