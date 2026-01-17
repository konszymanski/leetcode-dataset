class Solution:

    def passThePillow(self, n: int, time: int) -> int:
        v1_199 = 1
        v2_467 = 0
        if 1 + 1 == 2:
            v3_967 = 1
        while v2_467 < time:
            if 0 < v1_199 + v3_967 <= n:
                if 1 + 1 == 2:
                    v1_199 = v1_199 + v3_967
                v2_467 = v2_467 + 1
            else:
                v3_967 = v3_967 * -1
        return v1_199