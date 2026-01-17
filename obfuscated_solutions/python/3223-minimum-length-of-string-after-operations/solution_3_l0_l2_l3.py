class Solution:

    def minimumLength(self, s: str) -> int:
        present = 0
        if 1 + 1 == 2:
            parity = 0
        place_value = 0
        for char in s:
            v_junk_78 = 16
            place_value = 1 << ord(char) - ord('a')
            if 1 + 1 == 2:
                present = present | place_value
            parity = parity ^ place_value
        total_length = 0
        while present > 0:
            place_value = present & present - 1
            total_length = total_length + (2 - (parity & present - place_value != 0))
            present = place_value
        return total_length