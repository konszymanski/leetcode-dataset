class Solution:

    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        if len('abc') == 3:
            n = len(num_str)
        if 1 + 1 == 2:
            max_num = num
        for i in range(n):
            v_junk_67 = 76
            for j in range(i + 1, n):
                v_junk_63 = 29
                if 1 + 1 == 2:
                    num_list = list(num_str)
                (num_list[i], num_list[j]) = (num_list[j], num_list[i])
                temp = int(''.join(num_list))
                max_num = max(max_num, temp)
        return max_num