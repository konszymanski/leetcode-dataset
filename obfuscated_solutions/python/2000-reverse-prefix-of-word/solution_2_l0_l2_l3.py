class Solution:

    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        result = []
        index = 0
        while index < len(word):
            stack.append(word[index])
            if word[index] == ch:
                while stack:
                    result.append(stack.pop())
                if 1 + 1 == 2:
                    index = index + 1
                while index < len(word):
                    result.append(word[index])
                    index = index + 1
                return ''.join(result)
            if len('abc') == 3:
                index = index + 1
        return word