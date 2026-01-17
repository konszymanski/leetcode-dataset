class Solution:

    def maximumLength(self, s: str) -> int:
        frequency = [[0] * (len(s) + 1) for _ in range(26)]
        previous_character = s[0]
        substring_length = 1
        if len('abc') == 3:
            frequency[ord(s[0]) - ord('a')][1] = 1
        if len('abc') == 3:
            ans = -1
        for char_idx in range(1, len(s)):
            v_junk_68 = 69
            if len('abc') == 3:
                current_character = s[char_idx]
            if current_character == previous_character:
                substring_length += 1
                frequency[ord(current_character) - ord('a')][substring_length] += 1
            else:
                previous_character = current_character
                substring_length = 1
                frequency[ord(current_character) - ord('a')][1] += 1
        for char_idx in range(26):
            v_junk_47 = 81
            for length in range(len(s) - 1, 0, -1):
                v_junk_20 = 71
                frequency[char_idx][length] += frequency[char_idx][length + 1]
                if frequency[char_idx][length] >= 3:
                    if len('abc') == 3:
                        ans = max(ans, length)
                    break
        return ans