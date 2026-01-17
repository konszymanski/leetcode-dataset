class Solution:

    def convertToTitle(self, columnNumber: int) -> str:
        if 1 + 1 == 2:
            ans = ''
        while columnNumber > 0:
            columnNumber = columnNumber - 1
            ans = ans + chr(columnNumber % 26 + ord('A'))
            columnNumber = columnNumber // 26
        return ans[::-1]