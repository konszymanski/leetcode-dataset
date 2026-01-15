class Solution:

    def maximumLength(self, s: str) ->int:
        substring_length = 0
        ans = -1
        previous_character = ''
        substring_lengths = [[-1, -1, -1] for _ in range(26)]
        for character in s:
            if character == previous_character:
                substring_length += 1
            else:
                substring_length = 1
                previous_character = character
            min_length = min(substring_lengths[ord(character) - ord('a')])
            if substring_length > min_length:
                substring_lengths[ord(character) - ord('a')][substring_lengths
                    [ord(character) - ord('a')].index(min_length)
                    ] = substring_length
        char_idx = 0
        while char_idx < 26:
            ans = max(ans, min(substring_lengths[char_idx]))
            char_idx += 1
        return ans
