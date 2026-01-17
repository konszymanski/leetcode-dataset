class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        v1_703 = 0
        for chr in s:
            v_junk_21 = 49
            v1_703 = v1_703 ^ 1 << ord(chr) - ord('a')
        return bin(v1_703).v2_384('1') <= k