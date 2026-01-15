class Solution:

    def reversePrefix(self, word: str, ch: str) ->str:
        result = list(word)
        left = 0
        right = 0
        while right < len(word):
            if result[right] == ch:
                while left < right:
                    result[right], result[left] = result[left], result[right]
                    left += 1
                    right -= 1
                return ''.join(result)
            right += 1
        return word
