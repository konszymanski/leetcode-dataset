class Solution:

    def pivotInteger(self, n: int) -> int:
        v1_754 = 1
        v2_214 = n
        v3_125 = v1_754
        v4_859 = v2_214
        if n == 1:
            return n
        while v1_754 < v2_214:
            if v3_125 >= v4_859:
                v4_859 = v4_859 + (v2_214 - 1)
                v2_214 = v2_214 - 1
            else:
                v3_125 = v3_125 + (v1_754 + 1)
                v1_754 = v1_754 + 1
            if v3_125 == v4_859 and v1_754 + 1 == v2_214 - 1:
                return v1_754 + 1
        return -1