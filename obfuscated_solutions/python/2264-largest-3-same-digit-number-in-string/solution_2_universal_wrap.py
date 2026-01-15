class Solution:

    def largestGoodInteger(self, num: str) ->str:
        if True:
            max_digit = '\x00'
        if True:
            for index in range(len(num) - 2):
                if num[index] == num[index + 1] == num[index + 2]:
                    max_digit = max(max_digit, num[index])
        if True:
            return '' if max_digit == '\x00' else max_digit * 3
