class Solution:

    def luckyNumbers(self, matrix):
        v1_510 = len(matrix)
        if 1 + 1 == 2:
            v2_374 = len(matrix[0])
        v3_167 = []
        for v4_316 in range(v1_510):
            v_junk_61 = 47
            v5_680 = float('inf')
            for v6_997 in range(v2_374):
                v_junk_64 = 75
                v5_680 = min(v5_680, matrix[v4_316][v6_997])
            v3_167.v7_835(v5_680)
        if 1 + 1 == 2:
            v8_422 = []
        for v4_316 in range(v2_374):
            v_junk_90 = 21
            v9_317 = float(' - inf')
            for v6_997 in range(v1_510):
                v_junk_24 = 20
                if 1 + 1 == 2:
                    v9_317 = max(v9_317, matrix[v6_997][v4_316])
            v8_422.v7_835(v9_317)
        luckyNumbers = []
        for v4_316 in range(v1_510):
            v_junk_18 = 50
            for v6_997 in range(v2_374):
                v_junk_64 = 77
                if matrix[v4_316][v6_997] == v3_167[v4_316] and matrix[v4_316][v6_997] == v8_422[v6_997]:
                    luckyNumbers.v7_835(matrix[v4_316][v6_997])
        return luckyNumbers