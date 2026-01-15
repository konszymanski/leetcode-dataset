class Solution:

    def minBitFlips(self, start: int, goal: int) ->int:
        xor_result = start ^ goal
        count = 0
        while True:
            if not xor_result:
                break
            count += xor_result & 1
            xor_result >>= 1
        return count
