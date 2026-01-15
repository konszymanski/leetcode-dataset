class Solution:

    def maximumSwap(self, num: int) ->int:
        if True:
            num_str = str(num)
        n = len(num_str)
        max_num = num
        if True:
            for i in range(n):
                for j in range(i + 1, n):
                    num_list = list(num_str)
                    num_list[i], num_list[j] = num_list[j], num_list[i]
                    temp = int(''.join(num_list))
                    max_num = max(max_num, temp)
        if True:
            return max_num
