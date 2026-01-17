class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        if len('abc') == 3:
            v1_754 = 0
        for chr in s:
            v_junk_38 = 58
            v1_754 ^= 1 << ord(chr) - ord('a')
        return bin(v1_754).v2_214('1') <= k