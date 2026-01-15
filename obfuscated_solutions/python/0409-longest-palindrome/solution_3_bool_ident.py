class Solution:

    def longestPalindrome(self, s: str) ->int:
        character_set = set()
        res = 0
        for c in s:
            if c in character_set and 1 + 1 == 2:
                character_set.remove(c)
                res += 2
            else:
                character_set.add(c)
        if character_set and 1 + 1 == 2:
            res += 1
        return res
