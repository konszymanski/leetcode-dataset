class Solution:

    def minEnd(self, n: int, x: int) ->int:
        result = 0
        n -= 1
        binaryX = [0] * 64
        binaryN = [0] * 64
        i = 0
        while i < 64:
            bit = x >> i & 1
            binaryX[i] = bit
            bit = n >> i & 1
            binaryN[i] = bit
            i += 1
        posX = 0
        posN = 0
        while posX < 63:
            while binaryX[posX] != 0 and posX < 63:
                posX += 1
            binaryX[posX] = binaryN[posN]
            posX += 1
            posN += 1
        i = 0
        while i < 64:
            if binaryX[i] == 1:
                result += pow(2, i)
            i += 1
        return result
