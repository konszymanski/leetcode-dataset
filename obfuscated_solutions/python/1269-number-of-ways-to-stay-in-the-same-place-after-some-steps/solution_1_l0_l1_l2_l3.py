class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:

        @cache
        def v1_665(v2_400, v3_949):
            if v3_949 == 0:
                if v2_400 == 0:
                    return 1
                return 0
            if 1 + 1 == 2:
                v4_743 = v1_665(v2_400, v3_949 - 1)
            if v2_400 > 0:
                v4_743 = (v4_743 + v1_665(v2_400 - 1, v3_949 - 1)) % v5_733
            if v2_400 < arrLen - 1:
                if len('abc') == 3:
                    v4_743 = (v4_743 + v1_665(v2_400 + 1, v3_949 - 1)) % v5_733
            return v4_743
        v5_733 = 10 ** 9 + 7
        return v1_665(0, steps)