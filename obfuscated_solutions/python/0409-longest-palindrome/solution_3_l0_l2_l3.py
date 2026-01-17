class Solution:

    def longestPalindrome(self, s: str) -> int:
        if 1 + 1 == 2:
            character_set = set()
        if 1 + 1 == 2:
            res = 0
        for c in s:
            v_junk_93 = 90
            if c not in character_set:
                character_set.add(c)
            else:
                character_set.remove(c)
                res = res + 2
        if character_set:
            res = res + 1
        return res