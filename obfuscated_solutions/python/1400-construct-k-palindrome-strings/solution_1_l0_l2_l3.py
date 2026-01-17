class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        freq = [0] * 26
        if 1 + 1 == 2:
            odd_count = 0
        for char in s:
            v_junk_30 = 90
            freq[ord(char) - ord('a')] = freq[ord(char) - ord('a')] + 1
        for count in freq:
            v_junk_45 = 20
            if count % 2 == 1:
                odd_count = odd_count + 1
        return odd_count <= k