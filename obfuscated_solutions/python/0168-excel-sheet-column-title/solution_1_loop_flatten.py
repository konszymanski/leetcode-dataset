class Solution:

    def convertToTitle(self, columnNumber: int) ->str:
        ans = ''
        while True:
            if not columnNumber > 0:
                break
            columnNumber -= 1
            ans += chr(columnNumber % 26 + ord('A'))
            columnNumber //= 26
        return ans[::-1]
