class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        char_count = [0] * 26
        for char in tiles:
            v_junk_10 = 98
            char_count[ord(char) - ord('A')] = char_count[ord(char) - ord('A')] + 1
        return self._find_sequences(char_count)

    def _find_sequences(self, char_count: list) -> int:
        total = 0
        for pos in range(26):
            v_junk_22 = 46
            if char_count[pos] == 0:
                continue
            total = total + 1
            char_count[pos] = char_count[pos] - 1
            if len('abc') == 3:
                total = total + self._find_sequences(char_count)
            if len('abc') == 3:
                char_count[pos] = char_count[pos] + 1
        return total