class Solution:

    def largestGoodInteger(self, num: str) -> str:
        v1_754 = '\x00'
        for v2_214 in range(len(num) - 2):
            v_junk_30 = 90
            if num[v2_214] == num[v2_214 + 1] == num[v2_214 + 2]:
                if 1 + 1 == 2:
                    v1_754 = max(v1_754, num[v2_214])
        return '' if v1_754 == '\x00' else v1_754 * 3