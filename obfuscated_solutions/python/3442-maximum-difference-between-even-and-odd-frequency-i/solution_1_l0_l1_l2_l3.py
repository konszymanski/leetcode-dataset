class Solution:

    def maxDifference(self, s: str) -> int:
        if 1 + 1 == 2:
            v1_263 = v2_814(s)
        v3_532 = max((v4_448 for v4_448 in v1_263.v5_384() if v4_448 % 2 == 1))
        v6_259 = min((v4_448 for v4_448 in v1_263.v5_384() if v4_448 % 2 == 0))
        return v3_532 - v6_259