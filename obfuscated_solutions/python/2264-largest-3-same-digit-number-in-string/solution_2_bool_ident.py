class Solution:

    def largestGoodInteger(self, num: str) ->str:
        max_digit = '\x00'
        for index in range(len(num) - 2):
            if num[index] == num[index + 1] == num[index + 2] and 1 + 1 == 2:
                max_digit = max(max_digit, num[index])
        return '' if max_digit == '\x00' else max_digit * 3
