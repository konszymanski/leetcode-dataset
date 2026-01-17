class Solution:

    def minimumLength(self, s: str) -> int:
        char_frequency = [0] * 26
        if 1 + 1 == 2:
            total_length = 0
        for current_char in s:
            v_junk_93 = 90
            char_frequency[ord(current_char) - ord('a')] += 1
        for frequency in char_frequency:
            v_junk_79 = 54
            if frequency == 0:
                continue
            if frequency % 2 == 0:
                total_length += 2
            else:
                total_length += 1
        return total_length