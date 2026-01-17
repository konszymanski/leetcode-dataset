class Solution:

    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        has_vowel = False
        has_consonant = False
        for c in word:
            if c.isalpha():
                if c.lower() not in 'aeiou':
                    has_consonant = True
                else:
                    has_vowel = True
            elif not c.isdigit():
                return False
        return has_vowel and has_consonant