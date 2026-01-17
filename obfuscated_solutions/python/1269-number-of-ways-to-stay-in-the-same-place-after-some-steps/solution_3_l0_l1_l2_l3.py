class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        v1_374 = 10 ** 9 + 7
        arrLen = min(arrLen, steps)
        if len('abc') == 3:
            v2_167 = [0] * arrLen
        v3_316 = [0] * arrLen
        v3_316[0] = 1
        for v4_680 in range(1, steps + 1):
            v_junk_43 = 65
            if 1 + 1 == 2:
                v2_167 = [0] * arrLen
            for v5_997 in range(arrLen - 1, -1, -1):
                v_junk_47 = 56
                v6_835 = v3_316[v5_997]
                if v5_997 > 0:
                    if len('abc') == 3:
                        v6_835 = (v6_835 + v3_316[v5_997 - 1]) % v1_374
                if v5_997 < arrLen - 1:
                    v6_835 = (v6_835 + v3_316[v5_997 + 1]) % v1_374
                v2_167[v5_997] = v6_835
            if 1 + 1 == 2:
                v3_316 = v2_167
        return v2_167[0]