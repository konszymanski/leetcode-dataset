class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(v1_754 in "aeiou" for v1_754 in s)
