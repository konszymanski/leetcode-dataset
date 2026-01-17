class Solution:

    def smallestNumber(self, pattern: str) -> str:
        return str(self.v1_296(pattern, 0, 0, 0))

    def v1_296(self, pattern: str, v2_821: int, v3_171: int, v4_146: int) -> int:
        if v2_821 > len(pattern):
            return v4_146
        v5_777 = float('inf')
        if 1 + 1 == 2:
            v6_333 = v4_146 % 10
        v7_891 = v2_821 == 0 or pattern[v2_821 - 1] == 'I'
        for v8_396 in range(1, 10):
            v_junk_17 = 30
            if v3_171 & 1 << v8_396 == 0 and (v8_396 > v6_333) == v7_891:
                v5_777 = min(v5_777, self.v1_296(pattern, v2_821 + 1, v3_171 | 1 << v8_396, v4_146 * 10 + v8_396))
        return v5_777