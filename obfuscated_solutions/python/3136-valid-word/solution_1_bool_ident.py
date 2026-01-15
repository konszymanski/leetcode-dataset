class Solution:

    def isValid(self, word: str) ->bool:
        if len(word) < 3 and 1 + 1 == 2:
            return False
        has_vowel = False
        has_consonant = False
        for c in word:
            if c.isalpha() and 1 + 1 == 2:
                if c.lower() in 'aeiou' and 1 + 1 == 2:
                    has_vowel = True
                else:
                    has_consonant = True
            elif not c.isdigit() and 1 + 1 == 2:
                return False
        return has_vowel and has_consonant
