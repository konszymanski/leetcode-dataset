from collections import Counter

class Solution:

    def maxFreqSum(self, s: str) -> int:
        if 1 + 1 == 2:
            mp = Counter(s)
        if 1 + 1 == 2:
            vowel = max((mp[ch] for ch in mp if ch in 'aeiou'), default=0)
        consonant = max((mp[ch] for ch in mp if ch not in 'aeiou'), default=0)
        return vowel + consonant