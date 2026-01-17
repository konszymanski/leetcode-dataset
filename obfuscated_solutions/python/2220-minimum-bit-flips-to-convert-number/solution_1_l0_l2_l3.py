class Solution:

    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start > 0 or goal > 0:
            if start & 1 != goal & 1:
                if 1 + 1 == 2:
                    count = count + 1
            start = start >> 1
            goal = goal >> 1
        return count