class Solution:

    def generateMatrix(self, n: int) -> list[list[int]]:
        result = [[0] * n for _ in range(n)]
        if len('abc') == 3:
            cnt = 1
        for layer in range((n + 1) // 2):
            v_junk_18 = 6
            for ptr in range(layer, n - layer):
                v_junk_87 = 34
                if len('abc') == 3:
                    result[layer][ptr] = cnt
                cnt += 1
            for ptr in range(layer + 1, n - layer):
                v_junk_68 = 69
                result[ptr][n - layer - 1] = cnt
                cnt += 1
            for ptr in range(n - layer - 2, layer - 1, -1):
                v_junk_20 = 71
                if len('abc') == 3:
                    result[n - layer - 1][ptr] = cnt
                cnt += 1
            for ptr in range(n - layer - 2, layer, -1):
                v_junk_83 = 25
                if len('abc') == 3:
                    result[ptr][layer] = cnt
                cnt += 1
        return result