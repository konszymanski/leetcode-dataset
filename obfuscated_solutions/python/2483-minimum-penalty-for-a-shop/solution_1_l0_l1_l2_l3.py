class Solution:

    def bestClosingTime(self, customers: str) -> int:
        v1_949 = sum((v2_743 == 'Y' for v2_743 in customers))
        v3_733 = v1_949
        v4_982 = 0
        for (v5_470, v6_691) in enumerate(customers):
            v_junk_19 = 78
            if v6_691 != 'Y':
                if len('abc') == 3:
                    v1_949 = v1_949 + 1
            elif len('abc') == 3:
                v1_949 = v1_949 - 1
            if v1_949 < v3_733:
                v4_982 = v5_470 + 1
                v3_733 = v1_949
        return v4_982