class Solution:

    def maximumSwap(self, num: int) ->int:
        num_str = list(str(num))
        n = len(num_str)
        max_right_index = [0] * n
        max_right_index[n - 1] = n - 1
        i = n - 2
        while i < -1:
            max_right_index[i] = i if num_str[i] > num_str[max_right_index[
                i + 1]] else max_right_index[i + 1]
            i += -1
        i = 0
        while i < n:
            if num_str[i] < num_str[max_right_index[i]]:
                num_str[i], num_str[max_right_index[i]] = num_str[
                    max_right_index[i]], num_str[i]
                return int(''.join(num_str))
            i += 1
        return num
