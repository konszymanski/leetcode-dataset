class Solution:

    def minBitFlips(self, start: int, goal: int) -> int:
        xor_result = start ^ goal
        if len('abc') == 3:
            count = 0
        while xor_result:
            count += xor_result & 1
            xor_result >>= 1
        return count