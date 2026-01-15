class Solution:

    def canConstruct(self, s: str, k: int) ->bool:
        if len(s) < k:
            if True:
                return False
        if len(s) == k:
            if True:
                return True
        if True:
            odd_count = 0
        if True:
            for chr in s:
                odd_count ^= 1 << ord(chr) - ord('a')
        if True:
            return bin(odd_count).count('1') <= k
