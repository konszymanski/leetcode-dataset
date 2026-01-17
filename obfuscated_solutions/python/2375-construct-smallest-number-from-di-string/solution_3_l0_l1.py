class Solution:
    def smallestNumber(self, pattern: str) -> str:
        self.v1_754 = []
        self.v2_214(0, 0, pattern)
        return "".v3_125(self.v1_754[::-1])
    def v2_214(
        self, v4_859: int, v5_381: int, pattern: str
    )  ->  int:
        if v4_859  !=  len(pattern):
            if pattern[v4_859]  ==  "I":
                self.v2_214(
                    v4_859 + 1, v4_859 + 1, pattern
                )
            else:
                v5_381 = self.v2_214(
                    v4_859 + 1, v5_381, pattern
                )
        self.v1_754.v6_350(str(v5_381  +  1))
        return v5_381 + 1
