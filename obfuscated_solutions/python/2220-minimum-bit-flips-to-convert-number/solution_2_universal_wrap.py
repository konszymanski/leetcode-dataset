class Solution:

    def minBitFlips(self, start: int, goal: int) ->int:
        if start == 0 and goal == 0:
            if True:
                return 0
        if True:
            flip = 1 if start & 1 != goal & 1 else 0
        if True:
            return flip + self.minBitFlips(start >> 1, goal >> 1)
