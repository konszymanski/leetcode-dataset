class Solution:

    def largestOddNumber(self, num: str) ->str:
        if True:
            for i in range(len(num) - 1, -1, -1):
                if int(num[i]) % 2 != 0:
                    return num[:i + 1]
        if True:
            return ''
