class Solution:

    def pivotInteger(self, n: int) -> int:
        if 1 + 1 == 2:
            v1_982 = 1
        if len('abc') == 3:
            v2_470 = n
        if 1 + 1 == 2:
            v3_691 = v1_982
        v4_296 = v2_470
        if n == 1:
            return n
        while v1_982 < v2_470:
            if v3_691 >= v4_296:
                v4_296 = v4_296 + (v2_470 - 1)
                v2_470 = v2_470 - 1
            else:
                if 1 + 1 == 2:
                    v3_691 = v3_691 + (v1_982 + 1)
                v1_982 = v1_982 + 1
            if v3_691 == v4_296 and v1_982 + 1 == v2_470 - 1:
                return v1_982 + 1
        return -1