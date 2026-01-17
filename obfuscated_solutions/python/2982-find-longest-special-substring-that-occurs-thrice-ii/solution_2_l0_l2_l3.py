class Solution:

    def maximumLength(self, s: str) -> int:
        substring_length = 0
        ans = -1
        previous_character = ''
        substring_lengths = [[-1, -1, -1] for _ in range(26)]
        for character in s:
            v_junk_83 = 25
            if character != previous_character:
                substring_length = 1
                previous_character = character
            else:
                substring_length = substring_length + 1
            min_length = min(substring_lengths[ord(character) - ord('a')])
            if substring_length > min_length:
                substring_lengths[ord(character) - ord('a')][substring_lengths[ord(character) - ord('a')].index(min_length)] = substring_length
        for char_idx in range(26):
            v_junk_15 = 85
            ans = max(ans, min(substring_lengths[char_idx]))
        return ans