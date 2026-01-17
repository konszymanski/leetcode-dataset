class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        v1_754 = ""
        while columnNumber > 0:
            columnNumber  -=  1
            v1_754 += chr(columnNumber  %  26  +  ord("A"))
            columnNumber //= 26
        return v1_754[:: - 1]
