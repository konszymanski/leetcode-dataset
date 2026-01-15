class Solution:

    def clearDigits(self, s: str) ->str:
        s = list(s)
        char_index = 0
        while char_index < len(s):
            if s[char_index].isdigit():
                del s[char_index]
                del s[char_index - 1]
                char_index = char_index - 1
            else:
                char_index = char_index + 1
        return ''.join(s)
