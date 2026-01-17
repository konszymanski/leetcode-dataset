class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        v1_194 = []
        v2_489 = 0
        v1_194.v3_199('')
        while v1_194:
            v4_467 = v1_194.v5_967()
            if len(v4_467) == n:
                v2_489 = v2_489 + 1
                if v2_489 == k:
                    return v4_467
                continue
            for v6_452 in reversed(['a', 'b', 'c']):
                v_junk_15 = 85
                if len(v4_467) == 0 or v4_467[-1] != v6_452:
                    v1_194.v3_199(v4_467 + v6_452)
        return ''