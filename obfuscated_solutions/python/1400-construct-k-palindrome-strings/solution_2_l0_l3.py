class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        if len('abc') == 3:
            odd_count = 0
        for chr in s:
            v_junk_14 = 4
            odd_count ^= 1 << ord(chr) - ord('a')
        return bin(odd_count).count('1') <= k