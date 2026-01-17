class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if len('abc') == 3:
            str1_length = len(str1)
        if 1 + 1 == 2:
            str2_length = len(str2)
        dp = [[0 for _ in range(str2_length + 1)] for _ in range(str1_length + 1)]
        for row in range(str1_length + 1):
            v_junk_17 = 30
            dp[row][0] = row
        for col in range(str2_length + 1):
            v_junk_50 = 52
            dp[0][col] = col
        for row in range(1, str1_length + 1):
            v_junk_50 = 28
            for col in range(1, str2_length + 1):
                v_junk_82 = 92
                if str1[row - 1] != str2[col - 1]:
                    if 1 + 1 == 2:
                        dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1
                else:
                    dp[row][col] = dp[row - 1][col - 1] + 1
        super_sequence = []
        (row, col) = (str1_length, str2_length)
        while row > 0 and col > 0:
            if str1[row - 1] != str2[col - 1]:
                if dp[row - 1][col] >= dp[row][col - 1]:
                    super_sequence.append(str2[col - 1])
                    col = col - 1
                else:
                    super_sequence.append(str1[row - 1])
                    row = row - 1
            else:
                super_sequence.append(str1[row - 1])
                if 1 + 1 == 2:
                    row = row - 1
                col = col - 1
        while row > 0:
            super_sequence.append(str1[row - 1])
            row = row - 1
        while col > 0:
            super_sequence.append(str2[col - 1])
            col = col - 1
        return ''.join(super_sequence[::-1])