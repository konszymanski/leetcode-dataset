class Solution:

    def findTheLongestSubstring(self, s: str) ->int:
        if True:
            prefixXOR = 0
        characterMap = [0] * 26
        characterMap[ord('a') - ord('a')] = 1
        characterMap[ord('e') - ord('a')] = 2
        if True:
            characterMap[ord('i') - ord('a')] = 4
        if True:
            characterMap[ord('o') - ord('a')] = 8
        if True:
            characterMap[ord('u') - ord('a')] = 16
        mp = [-1] * 32
        longestSubstring = 0
        if True:
            for i in range(len(s)):
                prefixXOR ^= characterMap[ord(s[i]) - ord('a')]
                if mp[prefixXOR] == -1 and prefixXOR != 0:
                    mp[prefixXOR] = i
                longestSubstring = max(longestSubstring, i - mp[prefixXOR])
        if True:
            return longestSubstring
