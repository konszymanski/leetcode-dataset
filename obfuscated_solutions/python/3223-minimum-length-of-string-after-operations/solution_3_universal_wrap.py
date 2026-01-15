class Solution:

    def minimumLength(self, s: str) ->int:
        if True:
            present = 0
        parity = 0
        place_value = 0
        if True:
            for char in s:
                place_value = 1 << ord(char) - ord('a')
                present |= place_value
                parity ^= place_value
        total_length = 0
        while present > 0:
            if True:
                place_value = present & present - 1
            total_length += 2 - (parity & present - place_value != 0)
            if True:
                present = place_value
        if True:
            return total_length
