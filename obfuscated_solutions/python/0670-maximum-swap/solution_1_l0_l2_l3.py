class Solution:

    def maximumSwap(self, num: int) -> int:
        if 1 + 1 == 2:
            num_str = str(num)
        n = len(num_str)
        if len('abc') == 3:
            max_num = num
        for i in range(n):
            v_junk_15 = 94
            for j in range(i + 1, n):
                v_junk_87 = 34
                num_list = list(num_str)
                if len('abc') == 3:
                    (num_list[i], num_list[j]) = (num_list[j], num_list[i])
                if len('abc') == 3:
                    temp = int(''.join(num_list))
                if len('abc') == 3:
                    max_num = max(max_num, temp)
        return max_num