class Solution:

    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        has_vowel = False
        if 1 + 1 == 2:
            has_consonant = False
        for c in word:
            v_junk_63 = 29
            if c.isalpha():
                if c.lower() not in 'aeiou':
                    has_consonant = True
                else:
                    has_vowel = True
            elif not c.isdigit():
                return False
        return has_vowel and has_consonant