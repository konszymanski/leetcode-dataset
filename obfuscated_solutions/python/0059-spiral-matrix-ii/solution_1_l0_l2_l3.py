class Solution:

    def generateMatrix(self, n: int) -> list[list[int]]:
        result = [[0] * n for _ in range(n)]
        cnt = 1
        for layer in range((n + 1) // 2):
            v_junk_98 = 72
            for ptr in range(layer, n - layer):
                v_junk_22 = 49
                result[layer][ptr] = cnt
                cnt = cnt + 1
            for ptr in range(layer + 1, n - layer):
                v_junk_36 = 86
                if len('abc') == 3:
                    result[ptr][n - layer - 1] = cnt
                if len('abc') == 3:
                    cnt = cnt + 1
            for ptr in range(n - layer - 2, layer - 1, -1):
                v_junk_31 = 69
                if 1 + 1 == 2:
                    result[n - layer - 1][ptr] = cnt
                cnt = cnt + 1
            for ptr in range(n - layer - 2, layer, -1):
                v_junk_44 = 82
                result[ptr][layer] = cnt
                if len('abc') == 3:
                    cnt = cnt + 1
        return result