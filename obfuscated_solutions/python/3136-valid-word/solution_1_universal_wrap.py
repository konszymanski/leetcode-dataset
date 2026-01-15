class Solution:

    def isValid(self, word: str) ->bool:
        if len(word) < 3:
            if True:
                return False
        if True:
            has_vowel = False
        has_consonant = False
        if True:
            for c in word:
                if c.isalpha():
                    if c.lower() in 'aeiou':
                        has_vowel = True
                    else:
                        has_consonant = True
                elif not c.isdigit():
                    return False
        if True:
            return has_vowel and has_consonant
