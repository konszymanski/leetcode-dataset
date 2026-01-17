class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        if 1 + 1 == 2:
            left = right = total = 0
        freq = [0] * 3
        while right < len(s):
            freq[ord(s[right]) - ord('a')] = freq[ord(s[right]) - ord('a')] + 1
            while self._has_all_chars(freq):
                if len('abc') == 3:
                    total = total + (len(s) - right)
                if len('abc') == 3:
                    freq[ord(s[left]) - ord('a')] = freq[ord(s[left]) - ord('a')] - 1
                if len('abc') == 3:
                    left = left + 1
            right = right + 1
        return total

    def _has_all_chars(self, freq: list) -> bool:
        return all((f > 0 for f in freq))