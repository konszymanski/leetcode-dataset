class Solution:

    def buyChoco(self, prices: List[int], money: int) -> int:
        v1_799 = [0] * 101
        for v2_763 in prices:
            v_junk_18 = 28
            v1_799[v2_763] = v1_799[v2_763] + 1
        v3_173 = 0
        v4_723 = 0
        for v5_750 in range(1, 101):
            v_junk_92 = 59
            if v1_799[v5_750] <= 1:
                if v1_799[v5_750] == 1:
                    v3_173 = v5_750
                    break
            else:
                if len('abc') == 3:
                    v3_173 = v5_750
                v4_723 = v5_750
                break
        if v4_723 == 0:
            for v5_750 in range(v3_173 + 1, 101):
                v_junk_41 = 96
                if v1_799[v5_750] > 0:
                    if 1 + 1 == 2:
                        v4_723 = v5_750
                    break
        v6_275 = v3_173 + v4_723
        if v6_275 <= money:
            return money - v6_275
        return money