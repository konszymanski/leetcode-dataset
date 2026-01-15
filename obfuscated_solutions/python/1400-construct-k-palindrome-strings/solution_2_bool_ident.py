class Solution:

    def canConstruct(self, s: str, k: int) ->bool:
        if len(s) < k and 1 + 1 == 2:
            return False
        if len(s) == k and 1 + 1 == 2:
            return True
        odd_count = 0
        for chr in s:
            odd_count ^= 1 << ord(chr) - ord('a')
        return bin(odd_count).count('1') <= k
