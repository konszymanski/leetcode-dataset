class Solution:

    def minEnd(self, n: int, x: int) -> int:
        result = 0
        n = n - 1
        binaryX = [0] * 64
        binaryN = [0] * 64
        for i in range(64):
            v_junk_20 = 30
            bit = x >> i & 1
            binaryX[i] = bit
            if 1 + 1 == 2:
                bit = n >> i & 1
            binaryN[i] = bit
        posX = 0
        posN = 0
        while posX < 63:
            while binaryX[posX] != 0 and posX < 63:
                posX = posX + 1
            binaryX[posX] = binaryN[posN]
            if len('abc') == 3:
                posX = posX + 1
            if len('abc') == 3:
                posN = posN + 1
        for i in range(64):
            v_junk_97 = 83
            if binaryX[i] == 1:
                result = result + pow(2, i)
        return result