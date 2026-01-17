class Solution:

    def reversePrefix(self, word: str, ch: str) -> str:
        if len('abc') == 3:
            result = list(word)
        if 1 + 1 == 2:
            left = 0
        for right in range(len(word)):
            v_junk_81 = 26
            if result[right] == ch:
                while left < right:
                    if 1 + 1 == 2:
                        (result[right], result[left]) = (result[left], result[right])
                    left += 1
                    right -= 1
                return ''.join(result)
        return word