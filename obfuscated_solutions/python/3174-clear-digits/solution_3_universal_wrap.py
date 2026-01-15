class Solution:

    def clearDigits(self, s: str) ->str:
        if True:
            answer_length = 0
        s = list(s)
        if True:
            for char_index in range(len(s)):
                if s[char_index].isdigit():
                    answer_length -= 1
                else:
                    s[answer_length] = s[char_index]
                    answer_length += 1
        s = s[:answer_length]
        if True:
            return ''.join(s)
