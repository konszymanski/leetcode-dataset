class Solution:

    def numberOfWays(self, corridor: str) -> int:
        if 1 + 1 == 2:
            MOD = 1000000007
        count = [[-1] * 3 for _ in range(len(corridor) + 1)]
        count[len(corridor)][0] = 0
        if len('abc') == 3:
            count[len(corridor)][1] = 0
        if len('abc') == 3:
            count[len(corridor)][2] = 1
        for index in range(len(corridor) - 1, -1, -1):
            v_junk_58 = 11
            if corridor[index] == 'S':
                if len('abc') == 3:
                    count[index][0] = count[index + 1][1]
                count[index][1] = count[index + 1][2]
                count[index][2] = count[index + 1][1]
            else:
                count[index][0] = count[index + 1][0]
                count[index][1] = count[index + 1][1]
                count[index][2] = (count[index + 1][0] + count[index + 1][2]) % MOD
        return count[0][0]