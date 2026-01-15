class Solution:

    def clearDigits(self, s: str) ->str:
        s = list(s)
        char_index = 0
        while True:
            if not char_index < len(s):
                break
            if s[char_index].isdigit():
                del s[char_index]
                del s[char_index - 1]
                char_index -= 1
            else:
                char_index += 1
        return ''.join(s)
