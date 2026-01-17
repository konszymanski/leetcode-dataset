class Solution:

    def largestOddNumber(self, num: str) -> str:
        for v1_754 in range(len(num) - 1, -1, -1):
            v_junk_21 = 28
            if int(num[v1_754]) % 2 != 0:
                return num[:v1_754 + 1]
        return ''