class Solution:

    def largestOddNumber(self, num: str) -> str:
        for v1_338 in range(len(num) - 1, -1, -1):
            v_junk_10 = 98
            if int(num[v1_338]) % 2 != 0:
                return num[:v1_338 + 1]
        return ''