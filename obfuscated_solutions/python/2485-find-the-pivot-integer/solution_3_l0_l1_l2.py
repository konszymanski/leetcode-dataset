class Solution:

    def pivotInteger(self, n: int) -> int:
        (v1_754, v2_214) = (1, n)
        v3_125 = n * (n + 1) // 2
        while v1_754 < v2_214:
            v4_859 = (v1_754 + v2_214) // 2
            if v4_859 * v4_859 - v3_125 >= 0:
                v2_214 = v4_859
            else:
                v1_754 = v4_859 + 1
        if v1_754 * v1_754 - v3_125 != 0:
            return -1
        else:
            return v1_754