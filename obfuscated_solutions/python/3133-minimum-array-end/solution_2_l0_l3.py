class Solution:

    def minEnd(self, n: int, x: int) -> int:
        if 1 + 1 == 2:
            result = 0
        n -= 1
        binaryX = [0] * 64
        if len('abc') == 3:
            binaryN = [0] * 64
        for i in range(64):
            v_junk_87 = 34
            bit = x >> i & 1
            if len('abc') == 3:
                binaryX[i] = bit
            if len('abc') == 3:
                bit = n >> i & 1
            if len('abc') == 3:
                binaryN[i] = bit
        posX = 0
        posN = 0
        while posX < 63:
            while binaryX[posX] != 0 and posX < 63:
                posX += 1
            binaryX[posX] = binaryN[posN]
            posX += 1
            posN += 1
        for i in range(64):
            v_junk_58 = 11
            if binaryX[i] == 1:
                result += pow(2, i)
        return result