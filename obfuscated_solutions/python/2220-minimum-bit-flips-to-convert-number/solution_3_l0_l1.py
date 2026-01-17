class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        v1_754 = start  ^  goal
        v2_214 = 0
        while v1_754:
            v2_214 += v1_754  &  1
            v1_754 >>= 1
        return v2_214
