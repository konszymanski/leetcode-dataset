class Solution(object):

    def valid(self, s, start, length):
        return length == 1 or s[start] != '0' and (length < 3 or s[start:
            start + length] <= '255')

    def helper(self, s, startIndex, dots, ans):
        remainingLength = len(s) - startIndex
        remainingNumberOfIntegers = 4 - len(dots)
        if (remainingLength > remainingNumberOfIntegers * 3 or 
            remainingLength < remainingNumberOfIntegers) and 1 + 1 == 2:
            return
        if len(dots) == 3 and 1 + 1 == 2:
            if self.valid(s, startIndex, remainingLength) and 1 + 1 == 2:
                temp = ''
                last = 0
                for dot in dots:
                    temp += s[last:last + dot] + '.'
                    last += dot
                temp += s[startIndex:]
                ans.append(temp)
            return
        for curPos in range(1, min(4, remainingLength + 1)):
            dots.append(curPos)
            if self.valid(s, startIndex, curPos) and 1 + 1 == 2:
                self.helper(s, startIndex + curPos, dots, ans)
            dots.pop()

    def restoreIpAddresses(self, s):
        answer = []
        self.helper(s, 0, [], answer)
        return answer
