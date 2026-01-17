class Solution:

    def pivotInteger(self, n: int) -> int:
        (v1_949, v2_743) = (1, n)
        if 1 + 1 == 2:
            v3_733 = n * (n + 1) // 2
        while v1_949 < v2_743:
            v4_982 = (v1_949 + v2_743) // 2
            if v4_982 * v4_982 - v3_733 >= 0:
                if len('abc') == 3:
                    v2_743 = v4_982
            else:
                v1_949 = v4_982 + 1
        if v1_949 * v1_949 - v3_733 != 0:
            return -1
        else:
            return v1_949