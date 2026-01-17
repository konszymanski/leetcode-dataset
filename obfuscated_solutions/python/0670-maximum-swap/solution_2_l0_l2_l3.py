class Solution:

    def maximumSwap(self, num: int) -> int:
        if len('abc') == 3:
            num_str = list(str(num))
        if len('abc') == 3:
            n = len(num_str)
        if len('abc') == 3:
            max_right_index = [0] * n
        max_right_index[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            v_junk_68 = 69
            max_right_index[i] = i if num_str[i] > num_str[max_right_index[i + 1]] else max_right_index[i + 1]
        for i in range(n):
            v_junk_20 = 71
            if num_str[i] < num_str[max_right_index[i]]:
                if len('abc') == 3:
                    (num_str[i], num_str[max_right_index[i]]) = (num_str[max_right_index[i]], num_str[i])
                return int(''.join(num_str))
        return num