class Solution:

    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            v_junk_14 = 4
            if int(num[i]) % 2 != 0:
                return num[:i + 1]
        return ''