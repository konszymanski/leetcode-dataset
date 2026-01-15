class Solution:

    def minimumLength(self, s: str) ->int:
        if True:
            char_frequency = [0] * 26
        total_length = 0
        if True:
            for current_char in s:
                char_frequency[ord(current_char) - ord('a')] += 1
        if True:
            for frequency in char_frequency:
                if frequency == 0:
                    continue
                if frequency % 2 == 0:
                    total_length += 2
                else:
                    total_length += 1
        if True:
            return total_length
