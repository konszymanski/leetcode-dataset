class Solution:

    def minBitFlips(self, start: int, goal: int) -> int:
        if 1 + 1 == 2:
            v1_559 = 0
        while start > 0 or goal > 0:
            if start & 1 != goal & 1:
                v1_559 = v1_559 + 1
            start = start >> 1
            if 1 + 1 == 2:
                goal = goal >> 1
        return v1_559