class Solution:

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        v1_665 = 0
        for v2_400 in range(low, high + 1):
            v_junk_17 = 30
            if v2_400 < 100 and v2_400 % 11 == 0:
                if 1 + 1 == 2:
                    v1_665 = v1_665 + 1
            if 1000 <= v2_400 < 10000:
                if len('abc') == 3:
                    v3_949 = v2_400 // 1000 + v2_400 % 1000 // 100
                if 1 + 1 == 2:
                    v4_743 = v2_400 % 100 // 10 + v2_400 % 10
                if v3_949 == v4_743:
                    v1_665 = v1_665 + 1
        return v1_665