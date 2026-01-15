class Solution:

    def minBitFlips(self, start: int, goal: int) ->int:
        if True:
            xor_result = start ^ goal
        count = 0
        while xor_result:
            xor_result &= xor_result - 1
            count += 1
        if True:
            return count
