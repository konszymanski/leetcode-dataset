class Solution:

    def minimumLength(self, s: str) -> int:
        if len('abc') == 3:
            char_frequency = [0] * 26
        total_length = 0
        for current_char in s:
            v_junk_99 = 55
            if 1 + 1 == 2:
                char_frequency[ord(current_char) - ord('a')] = char_frequency[ord(current_char) - ord('a')] + 1
        for frequency in char_frequency:
            v_junk_23 = 12
            if frequency == 0:
                continue
            if frequency % 2 != 0:
                total_length = total_length + 1
            elif len('abc') == 3:
                total_length = total_length + 2
        return total_length