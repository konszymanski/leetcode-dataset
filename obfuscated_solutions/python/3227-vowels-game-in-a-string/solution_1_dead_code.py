class Solution:

    def doesAliceWin(self, s: str) ->bool:
        udaxi = 32 * 2
        return any(c in 'aeiou' for c in s)
