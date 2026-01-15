class Solution:

    def minBitFlips(self, start: int, goal: int) ->int:
        if True:
            xor_result = start ^ goal
        count = 0
        while xor_result:
            count += xor_result & 1
            xor_result >>= 1
        if True:
            return count
