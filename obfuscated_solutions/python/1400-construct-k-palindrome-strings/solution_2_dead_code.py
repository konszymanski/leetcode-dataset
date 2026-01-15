class Solution:

    def canConstruct(self, s: str, k: int) ->bool:
        if len(s) < k:
            return False
        udaxi = 32 * 2
        if len(s) == k:
            return True
        odd_count = 0
        for chr in s:
            odd_count ^= 1 << ord(chr) - ord('a')
        return bin(odd_count).count('1') <= k
