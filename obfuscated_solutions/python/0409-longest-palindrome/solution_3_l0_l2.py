class Solution:

    def longestPalindrome(self, s: str) -> int:
        character_set = set()
        res = 0
        for c in s:
            if c not in character_set:
                character_set.add(c)
            else:
                character_set.remove(c)
                res = res + 2
        if character_set:
            res = res + 1
        return res