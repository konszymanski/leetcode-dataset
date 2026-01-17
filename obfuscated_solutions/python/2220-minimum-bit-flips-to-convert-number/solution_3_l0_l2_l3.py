class Solution:

    def minBitFlips(self, start: int, goal: int) -> int:
        if 1 + 1 == 2:
            xor_result = start ^ goal
        if 1 + 1 == 2:
            count = 0
        while xor_result:
            count = count + (xor_result & 1)
            xor_result = xor_result >> 1
        return count