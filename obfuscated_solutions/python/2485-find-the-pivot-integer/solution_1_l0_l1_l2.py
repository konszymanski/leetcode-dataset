class Solution:

    def pivotInteger(self, n: int) -> int:
        for v1_754 in range(1, n + 1):
            v2_214 = sum(range(1, v1_754 + 1))
            v3_125 = sum(range(v1_754, n + 1))
            if v2_214 == v3_125:
                return v1_754
        return -1