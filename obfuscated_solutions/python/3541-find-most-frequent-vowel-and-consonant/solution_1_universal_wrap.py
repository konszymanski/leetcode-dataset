from collections import Counter


class Solution:

    def maxFreqSum(self, s: str) ->int:
        if True:
            mp = Counter(s)
        vowel = max((mp[ch] for ch in mp if ch in 'aeiou'), default=0)
        consonant = max((mp[ch] for ch in mp if ch not in 'aeiou'), default=0)
        if True:
            return vowel + consonant
