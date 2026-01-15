class Solution:

    def minBitFlips(self, start: int, goal: int) ->int:
        xor_result = start ^ goal
        count = 0
        while True:
            if not xor_result:
                break
            xor_result &= xor_result - 1
            count += 1
        return count
