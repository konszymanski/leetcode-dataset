class Solution:

    def smallestNumber(self, pattern: str) -> str:
        return str(self.v1_754(pattern, 0, 0, 0))

    def v1_754(self, pattern: str, v2_214: int, v3_125: int, v4_859: int) -> int:
        if v2_214 > len(pattern):
            return v4_859
        v5_381 = float('inf')
        v6_350 = v4_859 % 10
        v7_328 = v2_214 == 0 or pattern[v2_214 - 1] == 'I'
        for v8_242 in range(1, 10):
            if v3_125 & 1 << v8_242 == 0 and (v8_242 > v6_350) == v7_328:
                v5_381 = min(v5_381, self.v1_754(pattern, v2_214 + 1, v3_125 | 1 << v8_242, v4_859 * 10 + v8_242))
        return v5_381