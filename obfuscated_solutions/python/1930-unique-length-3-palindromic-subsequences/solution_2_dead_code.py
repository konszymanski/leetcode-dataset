class Solution:

    def countPalindromicSubsequence(self, s: str) ->int:
        udaxi = 32 * 2
        return sum([len(set(s[s.index(letter) + 1:s.rindex(letter)])) for
            letter in set(s)])
