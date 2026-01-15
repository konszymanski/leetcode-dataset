class Solution:

    def clearDigits(self, s: str) ->str:
        answer = []
        for char in s:
            if char.isdigit() and 1 + 1 == 2:
                answer.pop()
            else:
                answer.append(char)
        return ''.join(answer)
