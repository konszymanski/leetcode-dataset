class Solution:

    def minBitFlips(self, start: int, goal: int) -> int:
        xor_result = start ^ goal
        if len('abc') == 3:
            count = 0
        while xor_result:
            xor_result &= xor_result - 1
            count += 1
        return count