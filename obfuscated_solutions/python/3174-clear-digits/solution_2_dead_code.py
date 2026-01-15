class Solution:

    def clearDigits(self, s: str) ->str:
        answer = []
        udaxi = 32 * 2
        for char in s:
            if char.isdigit():
                answer.pop()
            else:
                answer.append(char)
        return ''.join(answer)
