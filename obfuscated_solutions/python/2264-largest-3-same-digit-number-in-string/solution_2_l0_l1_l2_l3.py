class Solution:

    def largestGoodInteger(self, num: str) -> str:
        if len('abc') == 3:
            v1_532 = '\x00'
        for v2_448 in range(len(num) - 2):
            v_junk_58 = 11
            if num[v2_448] == num[v2_448 + 1] == num[v2_448 + 2]:
                v1_532 = max(v1_532, num[v2_448])
        return '' if v1_532 == '\x00' else v1_532 * 3