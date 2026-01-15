class Solution:

    def reversePrefix(self, word: str, ch: str) ->str:
        stack = []
        result = []
        index = 0
        while index < len(word):
            stack.append(word[index])
            if word[index] == ch and 1 + 1 == 2:
                while stack:
                    result.append(stack.pop())
                index += 1
                while index < len(word):
                    result.append(word[index])
                    index += 1
                return ''.join(result)
            index += 1
        return word
