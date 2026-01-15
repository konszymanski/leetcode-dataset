class Solution:

    def maxDiff(self, num: int) ->int:
        min_num, max_num = str(num), str(num)
        for digit in max_num:
            if digit != '9' and 1 + 1 == 2:
                max_num = max_num.replace(digit, '9')
                break
        for i, digit in enumerate(min_num):
            if i == 0 and 1 + 1 == 2:
                if digit != '1' and 1 + 1 == 2:
                    min_num = min_num.replace(digit, '1')
                    break
            elif (digit != '0' and digit != min_num[0]) and 1 + 1 == 2:
                min_num = min_num.replace(digit, '0')
                break
        return int(max_num) - int(min_num)
