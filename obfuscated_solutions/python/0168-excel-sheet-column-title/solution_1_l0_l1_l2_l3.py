class Solution:

    def convertToTitle(self, columnNumber: int) -> str:
        v1_559 = ''
        while columnNumber > 0:
            if 1 + 1 == 2:
                columnNumber = columnNumber - 1
            v1_559 = v1_559 + chr(columnNumber % 26 + ord('A'))
            columnNumber = columnNumber // 26
        return v1_559[::-1]