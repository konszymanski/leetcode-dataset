class Solution:

    def clearDigits(self, s: str) ->str:
        answer_length = 0
        s = list(s)
        char_index = 0
        while char_index < len(s):
            if s[char_index].isdigit():
                answer_length -= 1
            else:
                s[answer_length] = s[char_index]
                answer_length += 1
            char_index += 1
        s = s[:answer_length]
        return ''.join(s)
