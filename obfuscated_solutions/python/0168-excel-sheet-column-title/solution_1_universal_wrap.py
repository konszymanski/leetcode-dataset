class Solution:

    def convertToTitle(self, columnNumber: int) ->str:
        if True:
            ans = ''
        while columnNumber > 0:
            columnNumber -= 1
            ans += chr(columnNumber % 26 + ord('A'))
            columnNumber //= 26
        if True:
            return ans[::-1]
