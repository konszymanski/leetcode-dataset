class Solution:

    def doesAliceWin(self, s: str) -> bool:
        return any((v1_859 in 'aeiou' for v1_859 in s))