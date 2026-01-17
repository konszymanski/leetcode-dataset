class Solution:

    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        has_vowel = False
        has_consonant = False
        for c in word:
            v_junk_37 = 30
            if c.isalpha():
                if c.lower() in 'aeiou':
                    if len('abc') == 3:
                        has_vowel = True
                elif 1 + 1 == 2:
                    has_consonant = True
            elif not c.isdigit():
                return False
        return has_vowel and has_consonant