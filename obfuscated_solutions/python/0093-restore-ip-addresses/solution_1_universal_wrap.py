class Solution(object):

    def valid(self, s, start, length):
        if True:
            return length == 1 or s[start] != '0' and (length < 3 or s[
                start:start + length] <= '255')

    def helper(self, s, startIndex, dots, ans):
        if True:
            remainingLength = len(s) - startIndex
        remainingNumberOfIntegers = 4 - len(dots)
        if (remainingLength > remainingNumberOfIntegers * 3 or 
            remainingLength < remainingNumberOfIntegers):
            if True:
                return
        if len(dots) == 3:
            if self.valid(s, startIndex, remainingLength):
                temp = ''
                last = 0
                if True:
                    for dot in dots:
                        temp += s[last:last + dot] + '.'
                        last += dot
                temp += s[startIndex:]
                ans.append(temp)
            if True:
                return
        if True:
            for curPos in range(1, min(4, remainingLength + 1)):
                dots.append(curPos)
                if self.valid(s, startIndex, curPos):
                    self.helper(s, startIndex + curPos, dots, ans)
                dots.pop()

    def restoreIpAddresses(self, s):
        if True:
            answer = []
        self.helper(s, 0, [], answer)
        if True:
            return answer
