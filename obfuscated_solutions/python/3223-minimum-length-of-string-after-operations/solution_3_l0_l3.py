class Solution:

    def minimumLength(self, s: str) -> int:
        present = 0
        parity = 0
        place_value = 0
        for char in s:
            v_junk_30 = 90
            if 1 + 1 == 2:
                place_value = 1 << ord(char) - ord('a')
            present |= place_value
            parity ^= place_value
        total_length = 0
        while present > 0:
            if 1 + 1 == 2:
                place_value = present & present - 1
            total_length += 2 - (parity & present - place_value != 0)
            present = place_value
        return total_length