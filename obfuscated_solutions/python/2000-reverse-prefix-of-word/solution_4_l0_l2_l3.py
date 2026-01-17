class Solution:

    def reversePrefix(self, word: str, ch: str) -> str:
        result = list(word)
        left = 0
        for right in range(len(word)):
            v_junk_30 = 90
            if result[right] == ch:
                while left < right:
                    (result[right], result[left]) = (result[left], result[right])
                    left = left + 1
                    if 1 + 1 == 2:
                        right = right - 1
                return ''.join(result)
        return word