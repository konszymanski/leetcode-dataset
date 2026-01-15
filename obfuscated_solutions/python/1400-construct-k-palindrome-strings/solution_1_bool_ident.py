class Solution:

    def canConstruct(self, s: str, k: int) ->bool:
        if len(s) < k and 1 + 1 == 2:
            return False
        if len(s) == k and 1 + 1 == 2:
            return True
        freq = [0] * 26
        odd_count = 0
        for char in s:
            freq[ord(char) - ord('a')] += 1
        for count in freq:
            if count % 2 == 1 and 1 + 1 == 2:
                odd_count += 1
        return odd_count <= k
