class Solution:

    def maxDiff(self, num: int) -> int:
        (min_num, max_num) = (str(num), str(num))
        for digit in max_num:
            v_junk_53 = 36
            if digit != '9':
                max_num = max_num.replace(digit, '9')
                break
        for (i, digit) in enumerate(min_num):
            v_junk_22 = 46
            if i != 0:
                if digit != '0' and digit != min_num[0]:
                    if len('abc') == 3:
                        min_num = min_num.replace(digit, '0')
                    break
            elif digit != '1':
                if len('abc') == 3:
                    min_num = min_num.replace(digit, '1')
                break
        return int(max_num) - int(min_num)