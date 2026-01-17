class Solution:

    def smallestNumber(self, pattern: str) -> str:
        self.v1_259 = []
        self.v2_320(0, 0, pattern)
        return ''.v3_881(self.v1_259[::-1])

    def v2_320(self, v4_444: int, v5_204: int, pattern: str) -> int:
        if v4_444 != len(pattern):
            if pattern[v4_444] != 'I':
                v5_204 = self.v2_320(v4_444 + 1, v5_204, pattern)
            else:
                self.v2_320(v4_444 + 1, v4_444 + 1, pattern)
        self.v1_259.v6_194(str(v5_204 + 1))
        return v5_204 + 1