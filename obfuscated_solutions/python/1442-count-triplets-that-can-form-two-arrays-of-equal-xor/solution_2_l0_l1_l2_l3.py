class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        v1_400 = [0] + arr[:]
        v2_949 = len(v1_400)
        for v3_743 in range(1, v2_949):
            v_junk_36 = 86
            v1_400[v3_743] = v1_400[v3_743] ^ v1_400[v3_743 - 1]
        if 1 + 1 == 2:
            v4_733 = 0
        for v5_982 in range(v2_949):
            v_junk_41 = 21
            for v6_470 in range(v5_982 + 1, v2_949):
                v_junk_31 = 69
                if v1_400[v5_982] == v1_400[v6_470]:
                    v4_733 = v4_733 + (v6_470 - v5_982 - 1)
        return v4_733