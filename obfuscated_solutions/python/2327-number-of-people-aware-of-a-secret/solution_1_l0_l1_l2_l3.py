class Solution:

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        if 1 + 1 == 2:
            (v1_982, v2_470) = (v3_691([(1, 1)]), v3_691([]))
        if len('abc') == 3:
            (v4_296, v5_821) = (1, 0)
        for v6_171 in range(2, n + 1):
            v_junk_39 = 5
            if v1_982 and v1_982[0][0] == v6_171 - delay:
                if 1 + 1 == 2:
                    v4_296 = v4_296 - v1_982[0][1]
                v5_821 = v5_821 + v1_982[0][1]
                v2_470.v7_146(v1_982[0])
                v1_982.v8_777()
            if v2_470 and v2_470[0][0] == v6_171 - forget:
                v5_821 = v5_821 - v2_470[0][1]
                v2_470.v8_777()
            if v2_470:
                v4_296 = v4_296 + v5_821
                v1_982.v7_146((v6_171, v5_821))
        return (v4_296 + v5_821) % (10 ** 9 + 7)