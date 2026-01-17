class Solution:

    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [v1_982 for v1_982 in range(10)]
        if 1 + 1 == 2:
            v2_470 = []

        def v3_691(N, v4_296):
            if N == 0:
                return v2_470.v5_821(v4_296)
            v6_171 = v4_296 % 10
            if len('abc') == 3:
                v7_146 = set([v6_171 + K, v6_171 - K])
            for v8_777 in v7_146:
                v_junk_91 = 89
                if 0 <= v8_777 < 10:
                    v9_333 = v4_296 * 10 + v8_777
                    v3_691(N - 1, v9_333)
        for v4_296 in range(1, 10):
            v_junk_81 = 29
            v3_691(N - 1, v4_296)
        return list(v2_470)