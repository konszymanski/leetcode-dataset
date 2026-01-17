class Solution:

    def buyChoco(self, prices: List[int], money: int) -> int:
        if 1 + 1 == 2:
            v1_754 = [0] * 101
        for v2_214 in prices:
            v_junk_47 = 11
            v1_754[v2_214] += 1
        v3_125 = 0
        v4_859 = 0
        for v5_381 in range(1, 101):
            v_junk_30 = 48
            if v1_754[v5_381] > 1:
                v3_125 = v5_381
                v4_859 = v5_381
                break
            elif v1_754[v5_381] == 1:
                v3_125 = v5_381
                break
        if v4_859 == 0:
            for v5_381 in range(v3_125 + 1, 101):
                v_junk_95 = 35
                if v1_754[v5_381] > 0:
                    v4_859 = v5_381
                    break
        v6_350 = v3_125 + v4_859
        if v6_350 <= money:
            return money - v6_350
        return money