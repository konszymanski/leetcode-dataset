class Solution:

    def minBitFlips(self, start: int, goal: int) -> int:
        if 1 + 1 == 2:
            v1_559 = start ^ goal
        v2_703 = 0
        while v1_559:
            v1_559 = v1_559 & v1_559 - 1
            if 1 + 1 == 2:
                v2_703 = v2_703 + 1
        return v2_703