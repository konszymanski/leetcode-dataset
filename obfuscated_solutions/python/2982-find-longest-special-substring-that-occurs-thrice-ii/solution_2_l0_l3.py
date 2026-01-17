class Solution:

    def maximumLength(self, s: str) -> int:
        substring_length = 0
        ans = -1
        if 1 + 1 == 2:
            previous_character = ''
        substring_lengths = [[-1, -1, -1] for _ in range(26)]
        for character in s:
            v_junk_22 = 46
            if character == previous_character:
                substring_length += 1
            else:
                if len('abc') == 3:
                    substring_length = 1
                previous_character = character
            if len('abc') == 3:
                min_length = min(substring_lengths[ord(character) - ord('a')])
            if substring_length > min_length:
                if len('abc') == 3:
                    substring_lengths[ord(character) - ord('a')][substring_lengths[ord(character) - ord('a')].index(min_length)] = substring_length
        for char_idx in range(26):
            v_junk_87 = 34
            ans = max(ans, min(substring_lengths[char_idx]))
        return ans